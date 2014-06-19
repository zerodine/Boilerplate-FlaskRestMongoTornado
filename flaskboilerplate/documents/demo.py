#from .. import odm as db
from . import odm as db
from flask.ext.restful import fields
from ..libs import DefaultRepository
from mongoengine import signals, queryset_manager


class Demo(db.Document):

    resource_fields = {
        'id':           fields.String,
        'email':        fields.String,
        'first_name':   fields.String,
        'last_name':    fields.String,
    }


    email = db.StringField(required=True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)

    class DemoRepository(DefaultRepository):

        def __init__(self):
            self.document = Demo

    @queryset_manager
    def objects(doc_cls, queryset):
        return Demo.DemoRepository().filter_for_acl(queryset)