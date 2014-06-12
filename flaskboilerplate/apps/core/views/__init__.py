from flaskboilerplate.apps.core import coreApp as app
from flaskboilerplate.apps.core.views.demo import Demo

app.add_url_rule('/demo1', view_func=Demo.as_view('demo1'))