import os

class Config(object):
    SECRET_KEY = os.getenv("SECRET_KEY") or 'kdkjjj8932lkj1--=ldj?121!ddfj8l1;h'
    FLASK_DEBUG = os.getenv("FLASK_DEBUG") == "True"

    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
