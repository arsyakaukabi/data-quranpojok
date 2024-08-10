from domain.entities import Surah, Ayah


class QuranUseCase:
    def __init__(self, api, repository):
        self.api = api
        self.repository = repository

    def fetch_and_save_quran(self):
        # Fetch and save surahs
        surahs = self.api.fetch_surahs()
        for surah in surahs:
            surah_entity = Surah(
                id=surah["id"],
                name=surah["name_arabic"],
                english_name=surah["name_simple"],
                ayah_count=surah["verses_count"],
                bismillah_pre=surah["bismillah_pre"],
            )
            self.repository.save_surah(surah_entity)

        # Fetch and save ayahs
        for surah in surahs:
            ayahs_uthmani = self.api.fetch_ayahs_uthmani(surah["id"])
            ayahs_indopak = self.api.fetch_ayahs_indopak(surah["id"])
            ayahs_imlai = self.api.fetch_ayahs_imlai(surah["id"])

            ayahs_data = {
                ayah["id"]: {
                    "verse_number": ayah["verse_key"].split(":")[1],
                    "text_uthmani": ayah.get("text_uthmani", ""),
                    "text_indopak": next(
                        (
                            a.get("text_indopak", "")
                            for a in ayahs_indopak
                            if a["id"] == ayah["id"]
                        ),
                        "",
                    ),
                    "text_imlaei": next(
                        (
                            a.get("text_imlaei", "")
                            for a in ayahs_imlai
                            if a["id"] == ayah["id"]
                        ),
                        "",
                    ),
                }
                for ayah in ayahs_uthmani
            }

            for ayah in ayahs_uthmani:
                verse_number = ayah["verse_key"].split(":")[1]
                ayah_entity = Ayah(
                    id=ayah["id"],
                    surah_id=surah["id"],
                    verse_number=int(verse_number),
                    text_uthmani=ayah.get("text_uthmani", ""),
                    text_indopak=ayahs_data.get(ayah["id"], {}).get("text_indopak", ""),
                    text_imlaei=ayahs_data.get(ayah["id"], {}).get("text_imlaei", ""),
                )
                print("ayah_entity", ayah_entity)
                self.repository.save_ayah(ayah_entity)

        print("Fetch and save pages and juz numbers")
        # Fetch and save pages and juz numbers
        pages_data = self.api.fetch_all_pages()
        for page_number, verses in pages_data.items():
            for verse in verses:
                ayah_id = verse["id"]
                juz_number = verse["juz_number"]
                self.repository.update_ayah(
                    Ayah(id=ayah_id, page_number=page_number, juz_number=juz_number)
                )