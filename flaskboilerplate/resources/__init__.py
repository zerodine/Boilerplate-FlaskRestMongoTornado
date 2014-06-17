from flask import g
from demo import Demo

api = getattr(g, '_api', None)
api.add_resource(Demo, '/demo/<string:_email>', '/demos')