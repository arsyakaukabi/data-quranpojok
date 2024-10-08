# data/repository/quran_repository.py

from domain.entities import Surah, Ayah
from data.database.models import SurahModel, AyahModel, session

class QuranRepository:
    def save_surah(self, surah: Surah):
        surah_record = SurahModel(
            id=surah.id,
            name=surah.name,
            english_name=surah.english_name,
            bismillah_pre=surah.bismillah_pre,
            ayah_count=surah.ayah_count
        )
        session.add(surah_record)
        session.commit()

    def save_ayah(self, ayah: Ayah):
        ayah_record = AyahModel(
            id=ayah.id,
            surah_id=ayah.surah_id,
            verse_number=ayah.verse_number,
            text_uthmani=ayah.text_uthmani,
            text_indopak=ayah.text_indopak,
            text_imlaei=ayah.text_imlaei,
            page_number=ayah.page_number,
            juz_number=ayah.juz_number
        )
        session.add(ayah_record)
        session.commit()

    def update_ayah(self, ayah: Ayah):
        ayah_record = session.query(AyahModel).filter_by(id=ayah.id).first()
        if ayah_record:
            ayah_record.page_number = ayah.page_number
            ayah_record.juz_number = ayah.juz_number
            session.commit()
        else:
            self.save_ayah(ayah)  # Insert if not exists