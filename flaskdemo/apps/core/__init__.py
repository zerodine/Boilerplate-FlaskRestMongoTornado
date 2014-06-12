__author__ = 'tspycher'

from flask import Flask
from flask.ext import restful
from flask_restful.utils import cors


coreApp = Flask(__name__)
coreApp.config.from_object('flaskdemo.apps.core.config.Config')

coreApi = restful.Api(coreApp)
coreApi.decorators = [cors.crossdomain(origin=coreApp.config['CORS_ORIGIN'], methods=coreApp.config['CORS_METHODS'], headers=coreApp.config['CORS_HEADERS'])]

import flaskdemo.apps.core.views
import flaskdemo.apps.core.resources