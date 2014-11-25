from sqlalchemy import Column, Integer, String,  DateTime, Boolean
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from nmhvoice import db


class User(db.Model):
    __tablename__ = "users"
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(100), index=True)
    year = Column('year', Integer)
    email = Column('email', String(100), unique=True, index=True)
    password = Column('pw', String(100))
    registered_date = Column('registered_on', DateTime)
    status = Column('status', Boolean, default=True)

    def __init__(self, full_name, email, password):
        self.name = full_name
        self.email = email
        self.password = generate_password_hash(password)
        self.status = True
        self.registered_date = datetime.utcnow()

        year = 0
        try:
            year = int(email.split('@')[0][-2:])
        except ValueError:
            year = -2000
        finally:
            year += 2000
        self.year = year
        # If year == 0, faculty member.

    def is_authenticated(self):
        return True

    def is_active(self):
        return self.status

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User %r>' % (self.name)
