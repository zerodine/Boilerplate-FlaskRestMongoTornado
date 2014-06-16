from . import app
from flask import g
from flask_mongoengine import MongoEngine
from werkzeug._internal import _log
from werkzeug.local import LocalProxy

def get_odm():
    with app.app_context():
        db = getattr(g, '_odm', None)
        if db is None:
            _log('info', " * MongoDB Connection created")
            db = g._database = MongoEngine(app)
        return db

odm = LocalProxy(get_odm)

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_odm', None)
    if db is not None:
        _log('info', " * MongoDB Connection droped")
