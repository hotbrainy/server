import os
basedir = os.path.abspath(os.path.dirname(__file__))




class ApplicationConfig:

    SECRET_KEY = os.environ.get("SECRET_KEY", os.urandom(32))
    SECURITY_PASSWORD_SALT = os.environ.get("SECURITY_PASSWORD_SALT", os.urandom(32))
    DEBUG = True

    # SESSION_TYPE = "filesystem"
    # SESSION_PERMANENT = False
    # SESSION_USE_SIGNER = True


    PROPAGATE_EXCEPTIONS = True

    RECAPTCHA_USE_SSL = False
    RECAPTCHA_PUBLIC_KEY = 'public'
    RECAPTCHA_PRIVATE_KEY = 'private'
    RECAPTCHA_OPTIONS = {'theme': 'white'}


    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = os.environ.get("MAIL_PORT")
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_DEFAULT_SENDER = 'R-I Software <ri-team@ri.website.com>'


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", os.urandom(32))
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///dev.db"
    DEBUG = True
    # SQLALCHEMY_ECHO=True


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///dev.db"
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS= False

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SQLALCHEMY_ECHO = False
    TESTING = True