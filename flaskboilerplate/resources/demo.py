from flask.ext import restful

from ..documents import Demo as DemoDocument


class Demo(restful.Resource):


    @restful.marshal_with(DemoDocument.resource_fields)
    def get(self, _email):
        x = DemoDocument.objects(email=_email)[0]
        return x

    def post(self, _email):
        demo = DemoDocument()
        demo.email = _email
        demo.first_name = "John"
        demo.last_name = "Doe"
        demo.save()