# Quran Database Project

## Overview

This project involves creating a Quran database using PostgreSQL. Data is fetched from the [Quran API](https://api-docs.quran.com) and inserted into the database using SQLAlchemy.

## Requirements

- Python 3.8 or later
- PostgreSQL
- Required Python libraries

## Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/arsyakaukabi/data-quranpojok
   cd data-quranpojok
2. **Create a Virtual Environment**
   ```bash
    python -m venv venv
    source venv/bin/activate  # On Mac
    venv\Scripts\activate # On Windows
3. **Install Dependencies**
   ```bash
    pip install -r requirements.txt
3. **Create a .env File**
    
    Create a .env file in the root directory of the project and add the following environment variables:

    ```bash
    DB_USERNAME=postgres
    DB_PASSWORD=postgres
    DB_HOST=localhost
    DB_PORT=5432
    DB_NAME=quranpojok
5. **Run the Script**

    After setting up the environment and dependencies, run the script to fetch data and populate the database:

    ```bash
    python main.py
## Project Structure

- `api/quran_api.py`: Contains methods to fetch data from the Quran API.
- `data/database/models.py`: Defines the SQLAlchemy models for the database.
- `data/repository/quran_repository.py`: Contains methods to save and update data in the database.
- `domain/entities.py`: Defines the domain entities for Surah and Ayah.
- `usecase/quran_use_case.py`: Contains the use case logic for fetching and saving data.
- `main.py`: The entry point of the application.


## API Documentation
This project uses the Quran API provided by Quran.com. The API endpoints used in this project include:

- Fetch Surahs: `GET https://api.quran.com/api/v4/chapters`
- Fetch Ayahs (Uthmani): `GET https://api.quran.com/api/v4/quran/verses/uthmani?chapter_number={surah_id}`
- Fetch Ayahs (Indopak): `GET https://api.quran.com/api/v4/quran/verses/indopak?chapter_number={surah_id}`
- Fetch Ayahs (Imlaei): `GET https://api.quran.com/api/v4/quran/verses/imlaei?chapter_number={surah_id}`
- Fetch Ayahs by Page: `GET https://api.quran.com/api/v4/verses/by_page/{page_number}`


## Notes
- The .env file should not be committed to version control for security reasons. Ensure it is included in .gitignore.


## License

This project is licensed under the MIT License. See the LICENSE file for details.



`Feel free to modify the repository URL, adjust any specific setup instructions, or add additional information as needed!`




