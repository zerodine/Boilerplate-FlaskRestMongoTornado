from flask import current_app as app
from rsa import Rsa, RsaId
from demo import Demo

app.add_url_rule('/_rsa', view_func=Rsa.as_view('rsa'))
app.add_url_rule('/_rsa/id', view_func=RsaId.as_view('rsaid'))

app.add_url_rule('/demo1', view_func=Demo.as_view('demo1'))
