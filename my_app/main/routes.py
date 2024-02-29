from dotenv import load_dotenv
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from sqlalchemy.orm import joinedload
from sqlalchemy.sql import func

from my_app import app, db
from my_app.main import bp
from my_app.main.forms import ConsumptionForm, PriceForm
from my_app.models import Consumption, Invoice, Price

load_dotenv()


menu = [
    {"name": "Главная", "url": "/"},
    {"name": "Статистика", "url": "/stats"},
    {"name": "Платежные документы", "url": "/insert_docs"},
    {"name": "Тарифы", "url": "/insert_prices"},
]


@bp.route("/")
def index():
    url = url_for("main.index")
    title = "Главная"
    return render_template("index.html", menu=menu, url=url, title=title)


@bp.route("/insert_docs", methods=["POST", "GET"])
@login_required
def insert_docs():
    user = current_user
    url = url_for("main.insert_docs")
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
        redirect(url_for("main.show_docs"))

    return render_template(
        "insert_docs.html", title=title, menu=menu, url=url, form=form
    )


@bp.route("/show_docs")
@login_required
def show_docs():
    url = url_for("main.show_docs")
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
    next_url = url_for("main.show_docs", page=docs.next_num) if docs.has_next else None
    prev_url = url_for("main.show_docs", page=docs.prev_num) if docs.has_prev else None

    return render_template(
        "show_docs.html",
        url=url,
        title=title,
        docs=docs.items,
        next_url=next_url,
        prev_url=prev_url,
        paginate_obj=docs,
    )


@bp.route("/show_prices")
@login_required
def show_prices():
    url = url_for("main.show_prices")
    user = current_user
    title = "Мои тарифы"
    prices = (
        Price.query.filter_by(user_id=user.id).order_by(Price.created_at.desc()).all()
    )
    return render_template("show_prices.html", url=url, title=title, prices=prices)


# # конвертеры: path, int, float (<int:doc_num>)
@bp.route("/document/<doc_num>")
@login_required
def show_document(doc_num):
    return f"Пользователь: {doc_num}"


@bp.route("/insert_prices", methods=["POST", "GET"])
@login_required
def insert_prices():
    user = current_user
    url = url_for("main.insert_prices")
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
        redirect(url_for("main.show_prices"))

    return render_template(
        "insert_prices.html", title="Тарифы", menu=menu, url=url, form=form
    )


@bp.route("/stats")
@login_required
def stats():
    url = url_for("main.stats")
    title = "Статистика"
    user = current_user
    consumtion = (
        Consumption.query.filter_by(user_id=user.id)
        .options(joinedload(Consumption.invoice))
        .order_by(Consumption.invoice_date.asc())
        .limit(12)
    )
    avg_common_total_query = (
        db.session.query(func.avg(Invoice.common_total))
        .filter_by(user_id=user.id)
        .scalar()
    )
    avg_variable_total_query = (
        db.session.query(func.avg(Invoice.variable_total))
        .filter_by(user_id=user.id)
        .scalar()
    )
    avg_total_query = (
        db.session.query(func.avg(Invoice.total)).filter_by(user_id=user.id).scalar()
    )

    avgs = [
        {
            "name": "Среднее по зеленым зонам (руб.)",
            "value": round(avg_common_total_query, 2) if avg_common_total_query else 0,
        },
        {
            "name": "Среднее по оранжевым зонам (руб.)",
            "value": round(avg_variable_total_query, 2) if avg_variable_total_query else 0,
        },
        {"name": "Среднее общее (руб.)", "value": round(avg_total_query, 2) if avg_total_query else 0},
    ]

    return render_template(
        "stats.html", title=title, menu=menu, url=url, consumption=consumtion, avgs=avgs
    )
