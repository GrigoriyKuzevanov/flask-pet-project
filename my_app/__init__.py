import logging
from logging.handlers import SMTPHandler

from config import Config
from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_moment import Moment

from my_app.celery_init import celery_init_app

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
moment = Moment(app)
login = LoginManager(app)
login.login_view = "auth.login"
login.login_message = "Авторизуйтесь в сервисе, чтобы открыть эту страницу"
mail = Mail(app)

from my_app.errors import bp as errors_bp
app.register_blueprint(errors_bp)

from my_app.auth import bp as auth_bp
app.register_blueprint(auth_bp, url_prefix="/auth")

from my_app.main import bp as main_bp
app.register_blueprint(main_bp)

if not app.debug:
    if app.config["MAIL_SERVER"]:
        auth = None
        if app.config["MAIL_USERNAME"] or app.config["MAIL_PASSWORD"]:
            auth = (app.config["MAIL_USERNAME"], app.config["MAIL_PASSWORD"])
        secure = None
        if app.config["MAIL_USE_TLS"]:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config["MAIL_SERVER"], app.config["MAIL_PORT"]),
            fromaddr=app.config["MAIL_USERNAME"],
            toaddrs=app.config["ADMINS"],
            subject="Коммуналка Failure",
            credentials=auth,
            secure=secure,
        )
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

celery_app = celery_init_app(app)

from my_app import models
