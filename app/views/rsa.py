from flask import current_app, abort
from flask.views import View

class Rsa(View):
    def dispatch_request(self):
        rsa = current_app.config['SERVICE'].get('rsa')
        if rsa is not None:
            return rsa.dumpPublicKey()
        abort(404)

class RsaId(View):
    def dispatch_request(self):
        rsa = current_app.config['SERVICE'].get('rsa')
        if rsa is not None:
            return rsa.getId()
        abort(404)


