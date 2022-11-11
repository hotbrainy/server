import os
from flask_migrate import upgrade,migrate,init,stamp
from server.apps.app import create_app
import configparser
from server.tools.assists import getconfig
config = configparser.ConfigParser()
config.read('config.cfg')

app = create_app()

def deploy():
    app.app_context().push()
    
    try:
        stamp()
        migrate()
        upgrade()
    except ImportError:
        init()
        stamp()
        migrate()
        upgrade()

deploy()

if __name__ == '__main__':
    app.run(debug=True)


