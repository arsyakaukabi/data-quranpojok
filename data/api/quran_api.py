import requests


class QuranAPI:
    BASE_URL = "https://api.quran.com/api/v4/"

    def fetch_surahs(self):
        response = requests.get(f"{self.BASE_URL}chapters")
        return response.json()["chapters"]

    def fetch_ayahs_uthmani(self, surah_id):
        response = requests.get(
            f"{self.BASE_URL}quran/verses/uthmani?chapter_number={surah_id}"
        )
        return response.json()["verses"]
    
    def fetch_ayahs_indopak(self, surah_id):
        response = requests.get(
            f"{self.BASE_URL}quran/verses/indopak?chapter_number={surah_id}"
        )
        return response.json()["verses"]

    def fetch_ayahs_imlai(self, surah_id):
        response = requests.get(
            f"{self.BASE_URL}quran/verses/imlaei?chapter_number={surah_id}"
        )
        return response.json()["verses"]

