from . import odm as db
from flask.ext.restful import fields
from basedocument import Basedocument
#from mongoengine import queryset_manager

class Demo(Basedocument):
    resource_fields = {
        'id':           fields.String,
        'email':        fields.String,
        'first_name':   fields.String,
        'last_name':    fields.String,
    }

    email = db.StringField(required=True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)

    #@queryset_manager
    #def objects(doc_cls, queryset):
    #    ''' Override this method to customize the default query '''
    #    return queryset