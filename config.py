from os import getenv
from pathlib import Path

BADE_DIR = Path(__file__).resolve().parent
USERNAME = "u1127123_delitan"
PASSWORD = "LF76B8IvUzqbH61v"
DB_FILE = f"mysql+pymysql://{USERNAME}:{PASSWORD}@localhost/u1127123_delitant_flask"

SQLALCHEMY_DATABASE_URI = getenv(
    "SQLALCHEMY_DATABASE_URI",
    DB_FILE,
)


class Config:
    TESTING = False
    DBUG = False
    SECRET_KEY = "b1b24e83b8a133ed94d1c0e3de6b9136"
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI


class ProductionConfig(Config):
    SECRET_KEY = "bfe2e0c7b2621a7bc6cab98c9aeae4ce"


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
