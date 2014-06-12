from flaskboilerplate.apps.core import coreApi as api
from demo import Demo

api.add_resource(Demo, '/demo2')