class Default:
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres@localhost/postgres"


class Development(Default):
    DEBUG = True

