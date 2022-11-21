from datetime import datetime, timezone
from secrets import token_hex
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Boolean, ARRAY
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
import os, uuid
import psycopg2, pymysql
from werkzeug.security import generate_password_hash, check_password_hash
from configparser import ConfigParser
from server.tools.assists import getconfig
config = ConfigParser()
config.read('config.cfg')

### Default database is MySQL

database_path = os.getenv('DATABASE_URL')
print(database_path)
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
            us =   [User(first_name='Baby',email='baby',password='baby'),
                    User(first_name='John',email='john6@mail.com',password='123123'),
                    User(first_name='Brown',email='brown3434@mail.com',password='123456', role='owner', is_admin=True),
                    User(first_name='George',email='george567@mail.com',password='121212'),
                    User(first_name='Sarah',email='sarah23@mail.com',password='343434', role='worker'),
                    User(first_name='Hela',email='hela@mail.com',password='343434', role='worker'),
                    User(first_name='Marcus',email='marcus4567@mail.com',password='123123', role='admin', is_admin=True),
                    User(first_name='Alex',email='alex3456@mail.com',password='alex123', role='assistant')]
            for u in us:
                u.is_confirmed = True
                u.insert()
        
        except: pass
        


def db_drop_and_create_all():
    
    db.drop_all()
    db.create_all()
    try:
        us =   [User(first_name='Baby',email='baby',password='baby'),
                User(first_name='John',email='john6@mail.com',password='123123'),
                User(first_name='Brown',email='brown3434@mail.com',password='123456', role='owner', is_admin=True),
                User(first_name='George',email='george567@mail.com',password='121212'),
                User(first_name='Sarah',email='sarah23@mail.com',password='343434', role='worker'),
                User(first_name='Hela',email='hela@mail.com',password='343434', role='worker'),
                User(first_name='Marcus',email='marcus4567@mail.com',password='123123', role='admin', is_admin=True),
                User(first_name='Alex',email='alex3456@mail.com',password='alex123', role='assistant')]
        for u in us:
            u.is_confirmed = True
            u.insert()
    
    except: pass


class User(db.Model):
    __tablename__ = 'users'
    # mostly token_id or external_id is used, instead of id
    id = Column(Integer, primary_key=True)
    # external_id is used for jwt, not id or email
    external_id = Column(String(32), unique=True, nullable=False, default=lambda: uuid.uuid4().hex)
    token_id = Column(String(64), unique=True, nullable=False, default=lambda: token_hex(32))

    email = Column(String(100), nullable=False, unique=True)
    _password = Column(String, nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100))
    company_name = Column(String(100))
    phone_number = Column(String(100))

    
    role = Column(String(100), nullable=False, default='user')
    registered_on = Column(DateTime, default=datetime.now(timezone.utc))

    is_admin = Column(Boolean, nullable=False, default=False)
    is_confirmed = Column(Boolean, nullable=False, default=False)
    
    confirmed_on = Column(DateTime)
    
    @property
    def password(self):
        print("Password can not be read.")

    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password, method='sha256')

    def verify_password(self, password):
        return check_password_hash(self._password, password)

    def insert(self):
        self.email = self.email.lower()
        db.session.add(self)
        db.session.commit()
    def update(self):
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def get_all(self, short=False):
        if short:
            return {
            'external_id': self.external_id,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'company_name': self.company_name,
            'phone_number': self.phone_number,
            'role': self.role,
            'is_admin': self.is_admin,
        }
        return {
            'id': self.id,
            'external_id': self.external_id,
            'token_id': self.token_id,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'company_name': self.company_name,
            'phone_number': self.phone_number,
            'role': self.role,
            'is_admin': self.is_admin,
            'registered_on': self.registered_on,
            'is_confirmed': self.is_confirmed,
            'confirmed_on': self.confirmed_on
        }
    
    def __repr__(self):
        return "<User %r>" % self.id



