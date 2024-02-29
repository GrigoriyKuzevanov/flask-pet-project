from urllib.parse import quote as url_quote

from dotenv import load_dotenv
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from my_app import db
from my_app.auth import bp
from my_app.auth.forms import (LoginForm, ProfileForm, RegistrationForm,
                               ResetPasswordForm, ResetPasswordRequestForm)
from my_app.auth.mail import send_password_reset_email
from my_app.models import Company, User

load_dotenv()


menu = [
    {"name": "Главная", "url": "/"},
    {"name": "Статистика", "url": "/stats"},
    {"name": "Платежные документы", "url": "/insert_docs"},
    {"name": "Тарифы", "url": "/insert_prices"},
]


@bp.route("/login", methods=["POST", "GET"])
def login():
    url = url_for("auth.login")
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    form = LoginForm()
    if form.validate_on_submit() and request.method == "POST":
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Неверный логин или пароль", category="error")
            return redirect(url_for("auth.login"))
        login_user(user, remember=form.remember_me.data)
        flash(
            f"Пользователь {form.username.data} авторизован успешно", category="success"
        )
        next_page = request.args.get("next")
        if not next_page or url_quote(next_page).netloc != "":
            next_page = url_for("main.index")
        return redirect(next_page)

    return render_template(
        "auth/login.html", title="Авторизация", menu=menu, form=form, url=url
    )


@bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.index"))


@bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Вы успешно зарегестрировались в сервисе")
        return redirect(url_for("auth.login"))
    return render_template(
        "auth/register.html", title="Регистрация", form=form, menu=menu
    )


@bp.route("/profile/<username>", methods=["GET", "POST"])
@login_required
def profile(username):
    url = url_for("auth.profile", username=username)
    user = current_user
    title = "Профиль пользователя"
    companies = Company.query.all()
    companies_list = [(c.id, c.name) for c in companies]
    form = ProfileForm(
        obj=user, original_username=user.username, original_email=user.email
    )
    form.company.choices = companies_list
    if form.validate_on_submit() and request.method == "POST":
        user.username = form.username.data
        user.email = form.email.data
        user.first_name = form.first_name.data
        user.last_name = form.last_name.data
        user.company_id = form.company.data
        db.session.commit()
        flash("Профиль обновлен успешно")
        redirect(url)
    return render_template(
        "auth/profile.html", user=user, title=title, url=url, menu=menu, form=form
    )


@bp.route("/password_reset_request", methods=["GET", "POST"])
def password_reset_request():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    form = ResetPasswordRequestForm()
    title = "Сброс пароля"
    url = url_for("auth.password_reset_request")
    if form.validate_on_submit() and request.method == "POST":
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash("На указанный адрес отправлена инструкция по сбросу пароля")
        return redirect(url_for("auth.login"))

    return render_template(
        "auth/password_reset_request.html", title=title, url=url, form=form
    )


@bp.route("/reset_password/<token>", methods=["GET", "POST"])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    title = "Изменение пароля"
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for("main.index"))
    form = ResetPasswordForm()
    if form.validate_on_submit() and request.method == "POST":
        user.set_password(form.password.data)
        db.session.commit()
        flash("Пароль успешно изменен")
        return redirect(url_for("auth.login"))

    return render_template("auth/reset_password.html", title=title, form=form)
