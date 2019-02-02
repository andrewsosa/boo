import os

SQLITE_MEMORY_URI = "sqlite:///:memory:"


class Default:
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # SQLALCHEMY_DATABASE_URI = "postgresql://postgres@localhost/postgres"
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "SQLALCHEMY_DATABASE_URI", SQLITE_MEMORY_URI
    )


class Development(Default):
    DEBUG = True


class Test(Development):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = SQLITE_MEMORY_URI
