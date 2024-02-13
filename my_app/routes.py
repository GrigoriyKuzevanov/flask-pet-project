# from werkzeug.urls import url_parse
from urllib.parse import quote as url_quote

from dotenv import load_dotenv
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from sqlalchemy.orm import joinedload

from my_app import app, db
from my_app.forms import (ConsumptionForm, LoginForm, PriceForm, ProfileForm,
                          RegistrationForm, ResetPasswordForm,
                          ResetPasswordRequestForm)
from my_app.mail import send_password_reset_email
from my_app.models import Company, Consumption, Invoice, Price, User

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
    price = (
        Price.query.filter_by(user_id=user.id).order_by(Price.created_at.desc()).first()
    )
    obj = (
        Consumption.query.filter_by(user_id=user.id)
        .order_by(Consumption.created_at.desc())
        .first()
    )
    if obj:
        form = ConsumptionForm(obj=obj)
    else:
        form = ConsumptionForm()
    if form.validate_on_submit() and request.method == "POST":
        consumption = Consumption(
            user_id=user.id,
            invoice_date=form.invoice_date.data,
            tko=form.tko.data,
            maintenance_common=form.maintenance_common.data,
            drainage_common=form.drainage_common.data,
            cold_water_common=form.cold_water_common.data,
            hot_water_volume_common=form.hot_water_volume_common.data,
            hot_water_energy_common=form.hot_water_energy_common.data,
            electricity_common=form.electricity_common.data,
            heating=form.heating.data,
            cold_water=form.cold_water.data,
            hot_water_volume=form.hot_water_volume.data,
            hot_water_energy=form.hot_water_energy.data,
            drainage=form.drainage.data,
            electricity=form.electricity.data,
            gas=form.gas.data,
            renovation=form.renovation.data,
        )
        db.session.add(consumption)
        db.session.commit()

        invoice = Invoice(
            user_id=user.id,
            consumption_id=consumption.id,
            invoice_date=consumption.invoice_date,
            tko=round(form.tko.data * price.tko, 2),
            maintenance_common=round(
                form.maintenance_common.data * price.maintenance_common, 2
            ),
            drainage_common=round(form.drainage_common.data * price.drainage_common, 2),
            cold_water_common=round(
                form.cold_water_common.data * price.cold_water_common, 2
            ),
            hot_water_volume_common=round(
                form.hot_water_volume_common.data * price.hot_water_volume_common, 2
            ),
            hot_water_energy_common=round(
                form.hot_water_energy_common.data * price.hot_water_energy_common, 2
            ),
            electricity_common=round(
                form.electricity_common.data * price.electricity_common, 2
            ),
            heating=round(form.heating.data * price.heating, 2),
            cold_water=round(form.cold_water.data * price.cold_water, 2),
            hot_water_volume=round(
                form.hot_water_volume.data * price.hot_water_volume, 2
            ),
            hot_water_energy=round(
                form.hot_water_energy.data * price.hot_water_energy, 2
            ),
            drainage=round(form.drainage.data * price.drainage, 2),
            electricity=round(form.electricity.data * price.electricity, 2),
            gas=round(form.gas.data * price.gas, 2),
            renovation=round(form.renovation.data * price.renovation, 2),
            recalculation=form.recalculation.data,
        )

        invoice.common_total = (
            invoice.tko
            + invoice.maintenance_common
            + invoice.drainage_common
            + invoice.cold_water_common
            + invoice.hot_water_volume_common
            + invoice.hot_water_energy_common
            + invoice.electricity_common
            + invoice.renovation
        )

        invoice.variable_total = (
            invoice.heating
            + invoice.cold_water
            + invoice.hot_water_volume
            + invoice.hot_water_energy
            + invoice.drainage
            + invoice.electricity
            + invoice.gas
        )

        invoice.total = invoice.common_total + invoice.variable_total

        if form.recalculation.data:
            invoice.total += form.recalculation.data

        db.session.add(invoice)
        db.session.commit()
        flash("Данные внесены успешно")
        redirect(url_for("show_docs"))

    return render_template(
        "insert_docs.html", title=title, menu=menu, url=url, form=form
    )


@app.route("/show_docs")
@login_required
def show_docs():
    url = url_for("show_docs")
    title = "Мои документы"
    user = current_user
    page = request.args.get("page", 1, type=int)
    docs = (
        Consumption.query.filter_by(user_id=user.id)
        .options(joinedload(Consumption.invoice))
        .order_by(Consumption.invoice_date.desc())
        .paginate(page=page, per_page=app.config["POSTS_PER_PAGE"], error_out=False)
    )
    # docs = (
    #     Invoice.query.filter_by(user_id=user.id)
    #     .order_by(Invoice.invoice_date.desc())
    #     .paginate(page=page, per_page=app.config['POSTS_PER_PAGE'], error_out=False)
    # )
    next_url = url_for("show_docs", page=docs.next_num) if docs.has_next else None
    prev_url = url_for("show_docs", page=docs.prev_num) if docs.has_prev else None

    return render_template(
        "show_docs.html",
        url=url,
        title=title,
        docs=docs.items,
        next_url=next_url,
        prev_url=prev_url,
        paginate_obj=docs,
    )


@app.route("/show_prices")
@login_required
def show_prices():
    url = url_for("show_prices")
    user = current_user
    title = "Мои тарифы"
    prices = (
        Price.query.filter_by(user_id=user.id).order_by(Price.created_at.desc()).all()
    )
    return render_template("show_prices.html", url=url, title=title, prices=prices)


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
    obj = (
        Price.query.filter_by(user_id=user.id).order_by(Price.created_at.desc()).first()
    )
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
            hot_water_volume=form.hot_water_volume.data,
            hot_water_energy=form.hot_water_energy.data,
            drainage=form.drainage.data,
            electricity=form.electricity.data,
            gas=form.gas.data,
            renovation=form.renovation.data,
        )
        db.session.add(price)
        db.session.commit()
        flash("Данные внесены успешно")
        redirect(url_for("show_prices"))

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


@app.route("/password_reset_request", methods=["GET", "POST"])
def password_reset_request():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = ResetPasswordRequestForm()
    title = "Сброс пароля"
    url = url_for("password_reset_request")
    if form.validate_on_submit() and request.method == "POST":
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash("На указанный адрес отправлена инструкция по сбросу пароля")
        return redirect(url_for("login"))

    return render_template(
        "password_reset_request.html", title=title, url=url, form=form
    )


@app.route("/reset_password/<token>", methods=["GET", "POST"])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    title = "Изменение пароля"
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for("index"))
    form = ResetPasswordForm()
    if form.validate_on_submit() and request.method == "POST":
        user.set_password(form.password.data)
        db.session.commit()
        flash("Пароль успешно изменен")
        return redirect(url_for("login"))

    return render_template("reset_password.html", title=title, form=form)
