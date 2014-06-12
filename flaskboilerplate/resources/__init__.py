from .. import api
from demo import Demo


api.add_resource(Demo, '/demo2/<string:_email>')