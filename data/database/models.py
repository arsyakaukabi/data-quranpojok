from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

Base = declarative_base()

class SurahModel(Base):
    __tablename__ = "surahs"
    id = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String, nullable=False)
    english_name = Column(String, nullable=False)
    ayah_count = Column(Integer, nullable=False)
    bismillah_pre = Column(Boolean, nullable=False)

class AyahModel(Base):
    __tablename__ = "ayahs"
    id = Column(Integer, primary_key=True, autoincrement=False)
    surah_id = Column(Integer, nullable=False)
    verse_number = Column(Integer, nullable=False)
    text_uthmani = Column(String, nullable=True)
    text_indopak = Column(String, nullable=True)
    text_imlaei = Column(String, nullable=True)

# Load database credentials from .env
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Create the database engine
engine = create_engine(
    f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Drop all tables if they exist and then create them again
Base.metadata.drop_all(engine)  # Drop all existing tables
Base.metadata.create_all(engine)  # Create all tables again

Session = sessionmaker(bind=engine)
session = Session()
