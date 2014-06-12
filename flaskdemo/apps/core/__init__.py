__author__ = 'tspycher'

from flask import Flask
from flask.ext import restful

coreApp = Flask(__name__)
coreApi = restful.Api(coreApp)

import flaskdemo.apps.core.views
import flaskdemo.apps.core.resources
