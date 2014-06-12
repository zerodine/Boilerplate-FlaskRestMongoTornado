

class Config(object):
    SECRET_KEY = 'SOME_SECRET_KEY_HERE'

    CORS_ORIGIN = ['*']
    CORS_METHODS = ['POST', 'GET', 'PUT', 'DELETE', 'OPTIONS', 'HEAD']
    CORS_HEADERS = ['origin', 'accept', 'content-type', 'authorization']