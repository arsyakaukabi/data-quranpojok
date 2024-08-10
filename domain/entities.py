# domain/entities.py

class Surah:
    def __init__(self, id, name, english_name, ayah_count, bismillah_pre):
        self.id = id
        self.name = name
        self.english_name = english_name
        self.ayah_count = ayah_count
        self.bismillah_pre = bismillah_pre

# domain/entities.py

class Ayah:
    def __init__(self, id, surah_id=None, verse_number=None, text_uthmani=None, text_indopak=None, text_imlaei=None, page_number=None, juz_number=None):
        self.id = id
        self.surah_id = surah_id
        self.verse_number = verse_number
        self.text_uthmani = text_uthmani
        self.text_indopak = text_indopak
        self.text_imlaei = text_imlaei
        self.page_number = page_number
        self.juz_number = juz_number
