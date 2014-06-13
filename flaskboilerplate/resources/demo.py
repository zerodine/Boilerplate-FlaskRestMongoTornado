from flask import request
from flask.ext import restful
from flask.ext.restful import reqparse

from ..documents import Demo as DemoDocument


class Demo(restful.Resource):

    def parser(self):
        parser = reqparse.RequestParser()
        parser.add_argument('first_name', type=str)
        parser.add_argument('last_name', type=str)

        return parser

    @restful.marshal_with(DemoDocument.resource_fields)
    def get(self, _email = None):
        if _email is None:
            return tuple(DemoDocument.objects)
        doc = DemoDocument.DemoRepository().abortIfNotExists(email=_email)
        return doc

    @restful.marshal_with(DemoDocument.resource_fields)
    def post(self, _email):
        args = self.parser().parse_args()

        demo = DemoDocument()
        demo.email = _email
        demo.first_name = args['first_name']
        demo.last_name = args['last_name']
        demo.save()
        return demo