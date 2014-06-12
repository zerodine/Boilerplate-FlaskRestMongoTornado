from flask.ext import restful
from ..documents import Demo as DemoDocument

class Demo(restful.Resource):


    def get(self):
        return {'hello': 'world'}

    def post(self):
        demo = DemoDocument()
        demo.email = "john.doe@domain.tld"
        demo.first_name = "John"
        demo.last_name = "Doe"
        demo.save()