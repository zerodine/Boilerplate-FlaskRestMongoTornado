class Config(object):
    SECRET_KEY = 'SOME_SECRET_KEY_HERE'

    CORS_ORIGIN = ['*']
    CORS_METHODS = ['POST', 'GET', 'PUT', 'DELETE', 'OPTIONS', 'HEAD']
    CORS_HEADERS = ['origin', 'accept', 'content-type', 'authorization']

    MONGODB_SETTINGS = dict({
        "DB": "flaskdemo",
        #"USERNAME": "my_user_name",
        #"PASSWORD": "my_secret_password",
        "HOST": "localhost",
        "PORT": 27017,
        #"DEBUG_TB_PANELS": "flask.ext.mongoengine.panels.MongoDebugPanel"
    })

    OAUTH_ENDPOINT = None