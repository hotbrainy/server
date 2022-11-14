from datetime import datetime, timezone
from secrets import token_hex
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Boolean, ARRAY
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
import os, uuid
import psycopg2, pymysql
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from configparser import ConfigParser
from server.tools.assists import getconfig
config = ConfigParser()
config.read('config.cfg')

### Default database is MySQL

database_path = os.getenv('DATABASE_URL')
database_path = getconfig(config, 'DATABASE', 'database_url') if not database_path else database_path
database_path = 'sqlite:///sqlite.db' if not database_path else database_path




db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    with app.app_context():
        app.config["SQLALCHEMY_DATABASE_URI"] = database_path
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        db.app = app
        db.init_app(app)
        db.create_all()
        try:
            new_User = User(first_name='Baby',email='baby5@mail.com',password=generate_password_hash('123456', method='sha256'), token_id =token_hex(16))
            new_User.insert()
            new_User = User(first_name='John',email='john6@mail.com',password=generate_password_hash('123123', method='sha256'), token_id =token_hex(16))
            new_User.insert()
            new_User = User(first_name='George',email='george567@mail.com',password=generate_password_hash('121212', method='sha256'), token_id =token_hex(16))
            new_User.insert()
            new_User = User(first_name='Sarah',email='sarah23@mail.com',password=generate_password_hash('343434', method='sha256'), role='worker', token_id =token_hex(16))
            new_User.insert()
        except: pass
def db_drop_and_create_all():
        db.drop_all()
        db.create_all()
        

def uuid4token():
    return uuid.uuid4().hex

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    # mostly token_id is used, not id.
    token_id = Column(String(32), unique=True, nullable=False, default=token_hex(16))
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String, nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100))
    company_name = Column(String(100))
    phone_number = Column(String(100))

    role = Column(String(100), nullable=False, default='user')
    registered_on = Column(DateTime, default=datetime.now(timezone.utc))
    admin = Column(Boolean, nullable=False, default=False)
    confirmed = Column(Boolean, nullable=False, default=False)
    confirmed_on = Column(DateTime)
    

    def insert(self):
        db.session.add(self)
        db.session.commit()
    def update(self):
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def get_all(self):
        return {
            'id': self.id,
            'token_id': self.token_id,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'company_name': self.company_name,
            'phone_number': self.phone_number,
            'role': self.role,
            'admin': self.admin,
            'registered_on': self.registered_on
            
        }
    
    def __repr__(self):
        return "<User %r>" % self.id



