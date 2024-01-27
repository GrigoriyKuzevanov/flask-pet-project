import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

user = os.getenv('DB_USER')
psw = os.getenv('DB_PASSWORD')
name = os.getenv('DB_PASSWORD')
host = os.getenv('DB_PASSWORD')
port = os.getenv('DB_PASSWORD')

DSN = f'postgresql://{user}:{psw}@{host}:{port}/{name}'

engine = create_engine(DSN)
Session = sessionmaker(bind=engine)
