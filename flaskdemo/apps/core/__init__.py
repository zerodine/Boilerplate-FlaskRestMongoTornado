from flask import Flask
from flask.ext import restful
from flask_restful.utils import cors

# Configure the Application
coreApp = Flask(__name__)
coreApp.config.from_object('flaskdemo.apps.core.config.Config')

# Configure the Applications API
coreApi = restful.Api(coreApp)
coreApi.decorators = [cors.crossdomain(origin=coreApp.config['CORS_ORIGIN'], methods=coreApp.config['CORS_METHODS'], headers=coreApp.config['CORS_HEADERS'])]

# Load all further resources
import flaskdemo.apps.core.views
import flaskdemo.apps.core.resources