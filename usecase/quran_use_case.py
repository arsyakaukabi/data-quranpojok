from domain.entities import Surah, Ayah

class QuranUseCase:
    def __init__(self, api, repository):
        self.api = api
        self.repository = repository

    def fetch_and_save_quran(self):
        surahs = self.api.fetch_surahs()

        for surah in surahs:
            surah_entity = Surah(
                id=surah["id"],
                name=surah["name_arabic"],
                english_name=surah["name_simple"],
                ayah_count=surah["verses_count"],
                bismillah_pre=surah["bismillah_pre"]
            )
            self.repository.save_surah(surah_entity)

            # Fetch ayahs in different scripts
            ayahs_uthmani = self.api.fetch_ayahs_uthmani(surah["id"])
            ayahs_indopak = self.api.fetch_ayahs_indopak(surah["id"])
            ayahs_imlai = self.api.fetch_ayahs_imlai(surah["id"])

            for ayah in ayahs_uthmani:
                verse_number = ayah["verse_key"].split(":")[1]
                ayah_entity = Ayah(
                    id=ayah["id"],
                    surah_id=surah["id"],
                    verse_number=int(verse_number),
                    text_uthmani=ayah.get("text_uthmani", ""),
                    text_indopak=next((a.get("text_indopak", "") for a in ayahs_indopak if a["verse_key"] == ayah["verse_key"]), ""),
                    text_imlaei=next((a.get("text_imlaei", "") for a in ayahs_imlai if a["verse_key"] == ayah["verse_key"]), "")
                )
                print("ayah_entity",ayah_entity)
                self.repository.save_ayah(ayah_entity)
