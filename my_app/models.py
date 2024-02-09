# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String
from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from my_app import db, login


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))
    password_hash = db.Column(db.String(256))
    reg_at = db.Column(db.TIMESTAMP, index=True, default=datetime.utcnow)
    prices = db.relationship("Price", backref="user", lazy="dynamic")
    consumptions = db.relationship("Consumption", backref="user", lazy="dynamic")
    invoices = db.relationship("Invoice", backref="user", lazy="dynamic")
    company_id = db.Column(db.Integer, db.ForeignKey("companies.id"))

    def __repr__(self):
        return f"{self.username}"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Price(db.Model):
    __tablename__ = "prices"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    company_id = db.Column(db.Integer, db.ForeignKey("companies.id"))
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
    electricity = db.Column(db.Float(12))
    gas = db.Column(db.Float(12))
    renovation = db.Column(db.Float(12))

    def __repr__(self):
        return f"{self.created_at.strftime('%b')}-{self.id}"


class Company(db.Model):
    __tablename__ = "companies"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    prices = db.relationship("Price", backref="company", lazy="dynamic")
    users = db.relationship("User", backref="company", lazy="dynamic")
    email = db.Column(db.String(120), index=True, unique=True)
    website = db.Column(db.String(256))
    address = db.Column(db.String(512))
    phone = db.Column(db.String(120))
    emergency_phone = db.Column(db.String(120))

    def __repr__(self):
        return self.name


class Consumption(db.Model):
    __tablename__ = "consumption"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    invoice = db.relationship("Invoice", uselist=False, backref="consumption")
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
    electricity = db.Column(db.Float(12))
    gas = db.Column(db.Float(12))
    renovation = db.Column(db.Float(12))
    invoice_date = db.Column(db.Date, index=True)

    def __repr__(self):
        return f"{self.created_at.strftime('%b')}-{self.id}"


class Invoice(db.Model):
    __tablename__ = "invoices"

    id = db.Column(db.Integer, primary_key=True)
    consumption_id = db.Column(db.Integer, db.ForeignKey("consumption.id"))
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
    electricity = db.Column(db.Float(12))
    gas = db.Column(db.Float(12))
    renovation = db.Column(db.Float(12))

    invoice_date = db.Column(db.Date, index=True)

    recalculation = db.Column(db.Float(12))
    common_total = db.Column(db.Float(12))
    variable_total = db.Column(db.Float(12))
    total = db.Column(db.Float(12))

    def __repr__(self):
        return f"Invoice {self.id}, created at {self.created_at}"
