from flask import Flask
from flask.ext import restful
from flask.ext.mongoengine import MongoEngine
from flask_restful.utils import cors
from flask_debugtoolbar import DebugToolbarExtension

# Configure the Application
coreApp = Flask(__name__)
coreApp.config.from_object('flaskboilerplate.apps.core.config.Config')

# Configure the Applications API
coreApi = restful.Api(coreApp)
coreApi.decorators = [cors.crossdomain(origin=coreApp.config['CORS_ORIGIN'], methods=coreApp.config['CORS_METHODS'], headers=coreApp.config['CORS_HEADERS'])]

# Configure the Database Connections
odm = MongoEngine(coreApp)

# the toolbar is only enabled in debug mode:
coreApp.debug = True
toolbar = DebugToolbarExtension(coreApp)


# Load all further resources
from . import views
from . import resources