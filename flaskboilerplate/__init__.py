from flask import Flask
from flask.ext import restful
from flask_restful.utils import cors
from decorators import authenticate


def create_app():
    # Configure the Application
    app = Flask(__name__)
    with app.app_context():
        from flask import current_app, g

        # within this block, current_app points to app.
        current_app.config.from_object('flaskboilerplate.config.Config')

        from odm import odm

        # Configure the Applications API
        g._api = restful.Api(current_app)
        g._api.decorators = [
            authenticate(endpoint=current_app.config['OAUTH_ENDPOINT']),
            cors.crossdomain(origin=current_app.config['CORS_ORIGIN'], methods=current_app.config['CORS_METHODS'],headers=current_app.config['CORS_HEADERS'])
        ]

        #return current_app
        # Load all further resources
        from . import views
        from . import resources

        return app
