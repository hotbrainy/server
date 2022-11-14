import os
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_session import Session
from server.db.models import db, setup_db
from configparser import ConfigParser
from server.apps.auth import init_api_authentication
from server.apps.errorhandlers import init_errorhandlers
from server.apps.api import init_rest_api

config = ConfigParser()
config.read('config.cfg')

app = Flask(__name__, static_url_path='', template_folder='../../client', static_folder='../../client')
app.config.from_object("config")

MIGRATION_DIR = os.path.join('server','db', 'migrations')


def create_app(app=app, test_config=None):

    server_session = Session(app)


    cors = CORS(app, supports_credentials=True)
    migrate = Migrate(app, db, directory=MIGRATION_DIR)
    setup_db(app)
    # db_drop_and_create_all()

    init_api_authentication(app)
    init_rest_api(app)
    init_errorhandlers(app)
    


    return app




