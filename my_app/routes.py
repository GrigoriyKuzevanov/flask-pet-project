# from werkzeug.urls import url_parse
from urllib.parse import quote as url_quote

from dotenv import load_dotenv
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

from my_app import app, db
from my_app.forms import LoginForm, RegistrationForm, PriceForm
from my_app.models import User

load_dotenv()


menu = [
    {"name": "Главная", "url": "/"},
    {"name": "Платежные документы", "url": "/docs"},
    {"name": "Тарифы", "url": "/prices"},
    {"name": "Статистика", "url": "/stats"},
]


@app.route("/")
def index():
    url = url_for("index")
    title = "Главная"
    return render_template("index.html", menu=menu, url=url, title=title)


@app.route("/docs")
@login_required
def documents():
    url = url_for("documents")
    return render_template(
        "documents.html", title="Платежные документы", menu=menu, url=url
    )


# конвертеры: path, int, float (<int:doc_num>)
@app.route("/document/<doc_num>")
@login_required
def show_document(doc_num):
    return f"Пользователь: {doc_num}"


@app.route("/prices", methods=["POST", "GET"])
@login_required
def prices():
    url = url_for("prices")
    form = PriceForm()
    if request.method == "POST":
        if len(request.form["username"]) > 2:
            flash("Сообщение отправлено", category="success")
        else:
            flash("Ошибка отправки", category="error")

    return render_template("prices.html", title="Тарифы", menu=menu, url=url, form=form)


@app.route("/stats")
@login_required
def stats():
    url = url_for("stats")
    return render_template("stats.html", title="Статистика", menu=menu, url=url)


@app.route("/login", methods=["POST", "GET"])
def login():
    url = url_for("login")
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit() and request.method == "POST":
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Неверный логин или пароль", category="error")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        flash(
            f"Пользователь {form.username.data} авторизован успешно", category="success"
        )
        next_page = request.args.get("next")
        if not next_page or url_quote(next_page).netloc != "":
            next_page = url_for("index")
        return redirect(next_page)

    return render_template(
        "login.html", title="Авторизация", menu=menu, form=form, url=url
    )


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Вы успешно зарегестрировались в сервисе")
        return redirect(url_for("login"))
    return render_template("register.html", title="Регистрация", form=form, menu=menu)


@app.route("/profile/<username>")
@login_required
def profile(username):
    url = url_for("profile", username=username)
    title = "Профиль пользователя"
    user = User.query.filter_by(username=username).first_or_404()
    return render_template("profile.html", user=user, title=title, url=url, menu=menu)


@app.errorhandler(404)
def page_not_found(error):
    return (
        render_template("errors/page404.html", title="Страница не найдена", menu=menu),
        404,
    )


@app.errorhandler(500)
def server_error(error):
    return (
        render_template("errors/page500.html", title="Ошибка сервера", menu=menu),
        500,
    )
