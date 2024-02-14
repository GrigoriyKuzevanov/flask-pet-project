from my_app import app, db, celery_app
from my_app.models import Price, User


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, "Price": Price}
