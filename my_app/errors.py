from flask import render_template

from my_app import app, db


@app.errorhandler(404)
def page_not_found(error):
    return (
        render_template("errors/page404.html", title="Страница не найдена"),
        404,
    )


@app.errorhandler(500)
def server_error(error):
    db.session.rollback()
    return (
        render_template("errors/page500.html", title="Ошибка сервера"),
        500,
    )
