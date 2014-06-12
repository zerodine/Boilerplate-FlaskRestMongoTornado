from flaskboilerplate import odm as db
from flask.ext.restful import fields


class Demo(db.Document):

    resource_fields = {
        'email':        fields.String,
        'first_name':   fields.String,
        'last_name':    fields.String,
    }


    email = db.StringField(required=True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)