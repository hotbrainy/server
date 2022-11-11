from datetime import datetime, timezone
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Boolean, ARRAY
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
import os
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
        
        try:
            new_User = User(first_name='Baby',email='baby@mail.com',password=generate_password_hash('123456', method='sha256'))
            new_User.insert()
            new_User = User(first_name='John',email='john@mail.com',password=generate_password_hash('123123', method='sha256'))
            new_User.insert()

        except: pass


def db_drop_and_create_all():
        db.drop_all()
        db.create_all()


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100))
    company_name = Column(String(100))
    phone_number = Column(String(100))

    role = Column(String(100), nullable=False, default='user')
    registered_on = Column(DateTime, nullable=False, default=datetime.now(timezone.utc))
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



