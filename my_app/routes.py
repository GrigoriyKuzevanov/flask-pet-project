# from werkzeug.urls import url_parse
from urllib.parse import quote as url_quote

from dotenv import load_dotenv
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

from my_app import app, db
from my_app.forms import (ConsumptionForm, LoginForm, PriceForm, ProfileForm,
                          RegistrationForm)
from my_app.models import Company, Consumption, Price, User, Invoice

load_dotenv()


menu = [
    {"name": "Главная", "url": "/"},
    {"name": "Статистика", "url": "/stats"},
    {"name": "Платежные документы", "url": "/insert_docs"},
    {"name": "Тарифы", "url": "/insert_prices"},
]


@app.route("/")
def index():
    url = url_for("index")
    title = "Главная"
    return render_template("index.html", menu=menu, url=url, title=title)


@app.route("/insert_docs", methods=["POST", "GET"])
@login_required
def insert_docs():
    user = current_user
    url = url_for("insert_docs")
    title = "Внести документ"
    price = Price.query.filter_by(user_id=current_user.id).first()
    obj = Consumption.query.first()
    if obj:
        form = ConsumptionForm(obj=obj)
    else:
        form = ConsumptionForm()
    if form.validate_on_submit() and request.method == "POST":
        consumption = Consumption(
            user_id=user.id,
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

        invoice = Invoice(
            user_id=user.id,
            tko=round(form.tko.data * price.tko, 2),
            maintenance_common=round(form.maintenance_common.data * price.maintenance_common, 2),
            drainage_common=round(form.drainage_common.data * price.drainage_common, 2),
            cold_water_common=round(form.cold_water_common.data * price.cold_water_common, 2),
            hot_water_volume_common=round(form.hot_water_volume_common.data * price.hot_water_volume_common, 2),
            hot_water_energy_common=round(form.hot_water_energy_common.data * price.hot_water_energy_common, 2),
            electricity_common=round(form.electricity_common.data * price.electricity_common, 2),
            heating=round(form.heating.data * price.heating, 2),
            cold_water=round(form.cold_water.data * price.cold_water, 2),
            hot_water_volume=round(form.hot_water_volume.data * price.hot_water_volume, 2),
            hot_water_energy=round(form.hot_water_energy.data * price.hot_water_energy, 2),
            drainage=round(form.drainage.data * price.drainage, 2),
            gas=round(form.gas.data * price.gas, 2),
            renovation=round(form.renovation.data * price.renovation, 2),
        )

        db.session.add(consumption)
        db.session.add(invoice)
        db.session.commit()
        flash("Данные внесены успешно")
        redirect(url_for("show_docs"))

    return render_template(
        "insert_docs.html", title=title, menu=menu, url=url, form=form
    )


@app.route("/show_docs")
def show_docs():
    url = url_for("show_docs")
    title = "Мои документы"
    docs = Consumption.query.all()
    return render_template("show_docs.html", url=url, title=title, docs=docs)


@app.route("/show_prices")
def show_prices():
    url = url_for("show_prices")
    title = "Мои тарифы"
    return render_template("show_prices.html", url=url, title=title)


# # конвертеры: path, int, float (<int:doc_num>)
@app.route("/document/<doc_num>")
@login_required
def show_document(doc_num):
    return f"Пользователь: {doc_num}"


@app.route("/insert_prices", methods=["POST", "GET"])
@login_required
def insert_prices():
    user = current_user
    url = url_for("insert_prices")
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

    return render_template(
        "insert_prices.html", title="Тарифы", menu=menu, url=url, form=form
    )


@app.route("/stats")
@login_required
def stats():
    url = url_for("stats")
    title = "Статистика"
    return render_template("stats.html", title=title, menu=menu, url=url)


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
        "profile.html", user=user, title=title, url=url, menu=menu, form=form
    )
