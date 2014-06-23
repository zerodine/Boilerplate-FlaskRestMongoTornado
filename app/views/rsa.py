from flask import current_app
from flask.views import View


class Rsa(View):
    def dispatch_request(self):
        rsa = current_app.config['SERVICE'].get('rsa')
        return rsa.dumpPublicKey()

class RsaId(View):
    def dispatch_request(self):
        rsa = current_app.config['SERVICE'].get('rsa')
        return rsa.getId()