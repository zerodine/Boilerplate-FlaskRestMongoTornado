from flask import g, current_app
from flask_mongoengine import MongoEngine
from werkzeug._internal import _log
from werkzeug.local import LocalProxy

def get_odm():
    """Form a complex number.

    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)
    """
    ctx = None
    db = getattr(g, '_odm', None)
    if db is None:
        _log('info', " * MongoDB Connection created DB Object %s in Context %s " % (hex(id(db)), hex(id(ctx))))
        db = g._odm = MongoEngine(current_app)
    return db

odm = LocalProxy(get_odm)
