from flask.ext import restful

from ..documents import Demo as DemoDocument
from ..documents import DemoRepository


class Demo(restful.Resource):

    @restful.marshal_with(DemoDocument.resource_fields)
    def get(self, _email):
        return DemoRepository().abortIfNotExists(email=_email)

    @restful.marshal_with(DemoDocument.resource_fields)
    def post(self, _email):
        demo = DemoDocument()
        demo.email = _email
        demo.first_name = "John"
        demo.last_name = "Doe"
        demo.save()
        return demo