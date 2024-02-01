# from werkzeug.urls import url_parse
from urllib.parse import quote as url_quote

from dotenv import load_dotenv
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

from my_app import app, db
from my_app.forms import LoginForm, PriceForm, ProfileForm, RegistrationForm
from my_app.models import Company, Price, User

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
    user = current_user
    url = url_for("prices")
    obj = Price.query.filter_by(user_id=user.id).order_by(Price.created_at).first()
    if obj:
        form = PriceForm(obj=obj)
    else:
        form = PriceForm()
    if form.validate_on_submit() and request.method == "POST":
        price = Price(
            user_id=user.id,
            company_id=user.company_id,
            tko=form.tko.data,
            maintenance_common=form.maintenance_common.data,
            drainage_common=form.drainage_common.data,
            cold_water_common=form.cold_water_common.data,
            hot_water_volume_common=form.hot_water_volume_common.data,
            hot_water_energy_common=form.hot_water_energy_common.data,
            electricity_common=form.electricity_common.data,
            heating=form.heating.data,
            cold_water=form.cold_water.data,
            hot_water_volume=form.cold_water.data,
            hot_water_energy=form.hot_water_energy.data,
            drainage=form.drainage.data,
            gas=form.gas.data,
            renovation=form.renovation.data,
        )
        db.session.add(price)
        db.session.commit()
        flash("Данные внесены успешно")
        redirect(url_for("prices"))

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


@app.route("/profile/<username>", methods=["GET", "POST"])
@login_required
def profile(username):
    url = url_for("profile", username=username)
    user = current_user
    title = f"Профиль пользователя <{user.username}>"
    title = "Профиль пользователя"
    companies = Company.query.all()
    companies_list = [(c.id, c.name) for c in companies]
    form = ProfileForm(obj=user)
    form.company.choices = companies_list
    if form.validate_on_submit() and request.method == "POST":
        user.username = form.username.data
        user.email = form.email.data
        user.company_id = form.company.data
        db.session.commit()
        flash("Профиль обновлен успешно")
        redirect(url)
    return render_template(
        "profile.html", user=user, title=title, url=url, menu=menu, form=form
    )


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
