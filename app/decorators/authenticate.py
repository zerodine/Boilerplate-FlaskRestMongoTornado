from functools import wraps
from flask import request, abort
from app.libs.authenticate import OAuth
from app.libs.authenticate import Signature
import base64


def authenticate(endpoint={}, node_key_allowed={}, node_key_cache_dir={}):
    """Verifies the given access token

    Keyword arguments:
    endpoint -- the API endpoint to verify the token (may configured at the config)
    """

    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):

            # Get the authorization header
            authorization = request.headers.get('Authorization')

            # Check if the header is present
            if authorization:

                # Split header into token (e.g. oauth token or signature) and mechanism (e.g. zda or bearer)
                token = authorization.split()[1]
                mechanism = authorization.split()[0]

                if mechanism.lower() == "zda":

                    # Helper method for header joining
                    def xstr(s):
                        return '' if s is None else str(s)

                    # Get a Signature instance
                    auth = Signature(node_key_allowed)

                    # Collect all attributes for a signature verify
                    token = base64.b64decode(token)
                    key_url = base64.b64decode(token.split(":")[0])
                    key_id = token.split(":")[1]
                    signature = token.split(":")[2]

                    # Create string to verify signature
                    # Inspired by http://docs.aws.amazon.com/AmazonS3/latest/dev/RESTAuthentication.html
                    string_to_verify = "\n".join([
                        xstr(request.method),
                        xstr(request.content_md5),
                        xstr(request.content_type),
                        xstr(request.date),
                        xstr(request.full_path)])

                    # Assign attributes to Signature instance
                    auth.string_to_verify = string_to_verify
                    auth.signature = signature
                    auth.key_id = key_id
                    auth.key_cache_dir = node_key_cache_dir

                    if key_url:
                        auth.key_url = key_url

                elif mechanism.lower() == "baerer":

                    # Get the OAuth instance
                    auth = OAuth(endpoint)

                    # Assign attributes to instance
                    auth.access_token = token

                else:

                    # Abort if no valid mechanism is given
                    abort(401)

                # If verification returns true: wuhuuu
                if auth.verify():
                    return f(*args, **kwargs)

            # Abort if something fails
            abort(401)

        return decorated_function

    return decorator