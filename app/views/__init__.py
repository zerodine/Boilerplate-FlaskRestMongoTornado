from rsa import Rsa, RsaId

def loadViews():
    from flask import current_app
    current_app.add_url_rule('/_rsa', view_func=Rsa.as_view('rsa'))
    current_app.add_url_rule('/_rsa/id', view_func=RsaId.as_view('rsaid'))

