# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String
from datetime import datetime

from my_app import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    reg_at = db.Column(db.TIMESTAMP, index=True, default=datetime.utcnow)
    prices = db.relationship("Price", backref="user", lazy="dynamic")

    def __repr__(self):
        return f"{self.username}"


class Price(db.Model):
    __tablename__ = "prices"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    created_at = db.Column(db.TIMESTAMP, index=True, default=datetime.utcnow)
    tko = db.Column(db.Float(12))
    maintenance_common = db.Column(db.Float(12))
    drainage_common = db.Column(db.Float(12))
    cold_water_common = db.Column(db.Float(12))
    hot_water_volume_common = db.Column(db.Float(12))
    hot_water_energy_common = db.Column(db.Float(12))
    electricity_common = db.Column(db.Float(12))
    heating = db.Column(db.Float(12))
    cold_water = db.Column(db.Float(12))
    hot_water_volume = db.Column(db.Float(12))
    hot_water_energy = db.Column(db.Float(12))
    drainage = db.Column(db.Float(12))
    gas = db.Column(db.Float(12))
    renovation = db.Column(db.Float(12))

    def __repr__(self):
        return f"for user {self.user_id}, created at {self.created_at}"
