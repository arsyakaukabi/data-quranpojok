# api/quran_api.py

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

    def fetch_ayahs_by_page(self, page_number):
        response = requests.get(f"{self.BASE_URL}verses/by_page/{page_number}")
        return response.json()["verses"]

    def fetch_all_pages(self):
        # Adjust the range as necessary to fetch all pages
        all_pages = {}
        for page_number in range(1, 605):  # Assuming there are 604 pages
            verses = self.fetch_ayahs_by_page(page_number)
            all_pages[page_number] = verses
        return all_pages
