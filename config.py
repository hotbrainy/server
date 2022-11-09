import os
basedir = os.path.abspath(os.path.dirname(__file__))


SECRET_KEY = os.urandom(32)
DEBUG = True

PROPAGATE_EXCEPTIONS = True

RECAPTCHA_USE_SSL = False
RECAPTCHA_PUBLIC_KEY = 'public'
RECAPTCHA_PRIVATE_KEY = 'private'
RECAPTCHA_OPTIONS = {'theme': 'white'}


MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USERNAME = 'eeee@gmail.com'
MAIL_PASSWORD = 'aaaabbbbccccdddd'
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEFAULT_SENDER = 'R-I Software <ri-team@ri.website.com>'

