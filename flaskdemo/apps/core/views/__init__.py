from flaskdemo.apps.core import coreApp as app
from flaskdemo.apps.core.views.demo import Demo

app.add_url_rule('/demo1', view_func=Demo.as_view('demo1'))