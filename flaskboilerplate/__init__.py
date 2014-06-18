from flask import Flask
from flask.ext import restful
from flask_restful.utils import cors
from decorators import authenticate
from flaskboilerplate.config.config_dev import Config


def create_app(env='dev', services = dict()):
    app = Flask(__name__)
    with app.app_context():
        from flask import current_app, g
        g._env = env
        current_app.config.from_object('flaskboilerplate.config.config_%s.Config' % env)

        # load all Services
        for name, obj in services.iteritems():
            app.config['SERVICE'].add(name, obj)

        from odm import odm

        # Configure the Applications API
        g._api = restful.Api(current_app)
        g._api.decorators = [
            authenticate(endpoint=current_app.config['OAUTH_ENDPOINT']),
            cors.crossdomain(origin=current_app.config['CORS_ORIGIN'], methods=current_app.config['CORS_METHODS'],headers=current_app.config['CORS_HEADERS'])
        ]

        # Load all further resources
        from . import views
        from . import resources

        return app
