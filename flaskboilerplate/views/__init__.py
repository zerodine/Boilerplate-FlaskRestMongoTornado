from flask import current_app as app
from demo import Demo


app.add_url_rule('/demo1', view_func=Demo.as_view('demo1'))