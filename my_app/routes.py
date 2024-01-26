import os

from dotenv import load_dotenv
from flask import flash, redirect, render_template, request, session, url_for

from my_app import app

load_dotenv()


app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["FLASK_DEBUG"] = os.getenv("FLASK_DEBUG") == "True"

menu = [
    {"name": "Главная", "url": "/"},
    {"name": "Платежные документы", "url": "/docs"},
    {"name": "Тарифы", "url": "/prices"},
    {"name": "Статистика", "url": "/stats"},
]


@app.route("/")
def index():
    url = url_for("index")
    return render_template("index.html", menu=menu, url=url)


@app.route("/docs")
def documents():
    url = url_for("documents")
    return render_template(
        "documents.html", title="Платежные документы", menu=menu, url=url
    )


# конвертеры: path, int, float (<int:doc_num>)
@app.route("/document/<doc_num>")
def show_document(doc_num):
    return f"Пользователь: {doc_num}"


@app.route("/prices", methods=["POST", "GET"])
def prices():
    url = url_for("prices")
    if request.method == "POST":
        if len(request.form["username"]) > 2:
            flash("Сообщение отправлено", category="success")
        else:
            flash("Ошибка отправки", category="error")

    return render_template("prices.html", title="Тарифы", menu=menu, url=url)


@app.route("/stats")
def stats():
    url = url_for("stats")
    return render_template("stats.html", title="Статистика", menu=menu, url=url)


@app.route("/login", methods=["POST", "GET"])
def login():
    if "userLogged" in session:
        return redirect(url_for("index", username=session["userLogged"]))
    elif (
        request.method == "POST"
        and request.form["username"] == "admin"
        and request.form["psw"] == "1234"
    ):
        session["userLogged"] = request.form["username"]
        return redirect(url_for("index", username=session["userLogged"]))

    return render_template("login.html", title="Авторизация", menu=menu)


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
