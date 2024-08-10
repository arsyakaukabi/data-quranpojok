from data.api.quran_api import QuranAPI
from data.database.repositories import QuranRepository
from usecase.quran_use_case import QuranUseCase


def main():
    api = QuranAPI()
    repository = QuranRepository()
    use_case = QuranUseCase(api, repository)

    use_case.fetch_and_save_quran()

if __name__ == "__main__":
    main()
