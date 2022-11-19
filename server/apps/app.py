import os
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from server.db.models import db, setup_db, db_drop_and_create_all
from configparser import ConfigParser
from config import ApplicationConfig
from server.apps.errorhandlers import init_app_errorhandlers
from server.apps.api import init_rest_api
from server.apps.auth import init_api_authentication

config = ConfigParser()
config.read('config.cfg')

app = Flask(__name__)
app.config.from_object(ApplicationConfig)
app.app_context().push()


def create_app(app=app, test_config=None):

    
    setup_db(app)


    CORS(app, supports_credentials=True)
    MIGRATION_DIR = os.path.join('server','db', 'migrations')
    migrate = Migrate(app, db, directory=MIGRATION_DIR)
    if test_config: db_drop_and_create_all()

    
    init_api_authentication(app)
    init_rest_api(app)
    init_app_errorhandlers(app)


    return app




