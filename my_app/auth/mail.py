from flask import render_template
from my_app import app
from my_app.tasks import send_email


def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email.delay(
        "[Коммуналка] Сброс пароля",
        sender=app.config["ADMINS"][0],
        recipients=[user.email],
        text_body=render_template("email/reset_password.txt", user=user, token=token),
        html_body=render_template("email/reset_password.html", user=user, token=token),
    )
