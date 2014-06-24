from flask import Flask, request
from flask.ext import restful
from flask_restful.utils import cors
from decorators import authenticate
from app.config.config_dev import Config

from libs.rsa import Rsa


def create_app(env='dev', services=dict()):
    # Create the flask app
    app = Flask(__name__)

    # Do everything in the app context
    with app.app_context():
        from flask import current_app, g

        g._env = env

        # Load the config
        current_app.config.from_object('app.config.config_%s.Config' % env)

        # Load all services
        for name, obj in services.iteritems():
            app.config['SERVICE'].add(name, obj)

        # Get the database connection object
        from odm import odm

        # Configure the Applications API
        g._api = restful.Api(current_app)
        g._api.decorators = [
            #authenticate(node_key_allowed=current_app.config['NODE_KEY_ALLOWED'], node_key_cache_dir=current_app.config['NODE_KEY_CACHE_DIR']),
            cors.crossdomain(origin=current_app.config['CORS_ORIGIN'], methods=current_app.config['CORS_METHODS'],
                             headers=current_app.config['CORS_HEADERS'])
        ]

        # Load all further resources
        from . import views
        from . import resources

        return app