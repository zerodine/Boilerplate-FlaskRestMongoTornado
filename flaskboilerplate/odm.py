from flask import g, current_app
from flask_mongoengine import MongoEngine
from werkzeug._internal import _log
from werkzeug.local import LocalProxy

def get_odm():
    #with current_app.app_context() as ctx:
    ctx = None
    db = getattr(g, '_odm', None)
    if db is None:
        _log('info', " * MongoDB Connection created DB Object %s in Context %s " % (hex(id(db)), hex(id(ctx))))
        db = g._odm = MongoEngine(current_app)
    return db

odm = LocalProxy(get_odm)
