from flask.ext import restful
from ..documents import Demo as DemoDocument


class Demo(restful.Resource):

    @restful.marshal_with(DemoDocument.resource_fields)
    def get(self, _email = None):
        if _email is None:
            return tuple(DemoDocument.objects)
        doc = DemoDocument.DemoRepository().abortIfNotExists(email=_email)
        return doc

    @restful.marshal_with(DemoDocument.resource_fields)
    def post(self, _email):
        demo = DemoDocument()
        demo.email = _email
        demo.first_name = "John"
        demo.last_name = "Doe"
        demo.save()
        return demo