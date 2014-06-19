from functools import wraps
from flask import request, abort
from flaskboilerplate.libs.oauth import OAuth


def authenticate(endpoint={}):
    """Verifies the given access token

    Keyword arguments:
    endpoint -- the API endpoint to verify the token (may configured at the config)
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):

            # Get the oauth lib and the header
            oauth = OAuth(endpoint)
            access_token = request.headers.get('Authorization')
            if endpoint is None and access_token is None:
                return f(*args, **kwargs)

            if access_token:
                if oauth.verify(access_token.split()[1]):
                    return f(*args, **kwargs)

            abort(401)

        return decorated_function
    return decorator