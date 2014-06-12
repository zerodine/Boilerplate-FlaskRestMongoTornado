from flask.views import View

class Demo(View):


    def dispatch_request(self):
        return 'Hello World!'