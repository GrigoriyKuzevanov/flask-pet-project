# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String
from my_app import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    reg_at = db.Column(db.TIMESTAMP, default=datetime.utcnow)

    def __repr__(self):
        return f'{self.username}'
    