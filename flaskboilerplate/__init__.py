from flask import Flask
from flask_mongoengine import MongoEngine
from flask.ext import restful
from flask_restful.utils import cors

# from flask_debugtoolbar import DebugToolbarExtension

# Configure the Application
app = Flask(__name__)
app.config.from_object('flaskboilerplate.config.Config')

# Configure the Applications API
api = restful.Api(app)

odm = MongoEngine(app)

api.decorators = [cors.crossdomain(origin=app.config['CORS_ORIGIN'], methods=app.config['CORS_METHODS'], headers=app.config['CORS_HEADERS'])]

# Load all further resources
from . import views
from . import resources