class ServiceContainer(object):
    _services = dict()

    def add(self, name, obj):
        """Add a to the service container

        Keyword arguments:
        name -- name of the service
        obj -- the service itself
        """
        self._services[name] = obj

    def get(self, name):
        """Get a service from the service container

        Keyword arguments:
        name -- name of the service
        """
        return self._services[name]


class Config(object):
    # Key used for salting or other stuff
    SECRET_KEY = 'SOME_SECRET_KEY_HERE'

    # Name for logger
    LOGGER_NAME = 'flaskboilerplate'

    # CORS settings for XHR-calls from browsers
    CORS_ORIGIN = ['*']
    CORS_METHODS = ['POST', 'GET', 'PUT', 'DELETE', 'OPTIONS', 'HEAD']
    CORS_HEADERS = ['origin', 'accept', 'content-type', 'authorization']

    # Connection settings for MongoDB support
    MONGODB_SETTINGS = dict({
        "DB": "flaskdemo",
        #"USERNAME": "my_user_name",
        #"PASSWORD": "my_secret_password",
        "HOST": "localhost",
        "PORT": 27017,
        #"DEBUG_TB_PANELS": "flask.ext.mongoengine.panels.MongoDebugPanel"
    })

    # If the access token given in a Authorization header should be verified
    OAUTH_ENDPOINT = None

    # Keys for signing auth
    NODE_KEY_ALLOWED = [
        # Test frontend
        "d7c86080232a7f61598cb55c5bcae63967421d33",
        # Another frontend
        "e7c86080262e7f61598cb5c5b1ae9396d421d483"
    ]

    NODE_KEY_CACHE_DIR = "../keycache/"

    # DO NOT CHANGE
    SERVICE = ServiceContainer()