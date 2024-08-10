from dataclasses import dataclass

@dataclass
class Surah:
    id: int
    name: str
    english_name: str
    ayah_count: int
    bismillah_pre: bool

@dataclass
class Ayah:
    id: int
    surah_id: int
    verse_number: int
    text_uthmani: str
    text_imlaei: str
    text_indopak: str


