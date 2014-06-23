from flask import g
from demo import Demo, DemoStats

# Get the api from context globals
api = getattr(g, '_api', None)

# Define the resources and routes
api.add_resource(Demo, '/demo/<string:_email>', '/demos')
api.add_resource(DemoStats, '/demostats')
#api.add_resource(AnotherResource, '/anotherresource/<string:name>', '/anotherressource')