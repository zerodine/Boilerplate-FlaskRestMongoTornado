import datetime, decimal
import mongoengine
from mongoengine.base.fields import BaseField as AbstractBaseField #, ObjectIdField
from flask.ext.restful import fields

from app.libs import DefaultRepository
#from app.libs.acl import AclAwareQueryset


class AbstractBasedocument(mongoengine.Document):
    meta = {'abstract': True}

    _deleted = mongoengine.BooleanField(default=False)
    created = mongoengine.DateTimeField(default=datetime.datetime.utcnow())
    updated = mongoengine.DateTimeField(default=datetime.datetime.utcnow())

    '''
    Contains information about every Mongoengine Field type conversion to marshal or requestparser
    '''
    _type_conversion = dict({
        'FileField':                {'marshal': fields.String, 'parser': str},
        'FloatField':               {'marshal': fields.Float, 'parser': float},
        'StringField':              {'marshal': fields.String, 'parser': str},
        'BinaryField':              {'marshal': fields.Raw, 'parser': bin},
        'BooleanField':             {'marshal': fields.Boolean, 'parser': bool},
        'ComplexDateTimeField':     {'marshal': fields.DateTime, 'parser': datetime},
        'DateTimeField':            {'marshal': fields.DateTime, 'parser': datetime},
        'DecimalField':             {'marshal': fields.MyDecimal, 'parser': decimal},
        'DictField':                {'marshal': fields.Raw, 'parser': dict},
        'DynamicField':             {'marshal': fields.Raw, 'parser': str},
        'EmailField':               {'marshal': fields.String, 'parser': str},
        'EmbeddedDocumentField':    {'marshal': fields.Raw, 'parser': str},
        'GeoPointField':            {'marshal': fields.Raw, 'parser': str},
        'ImageField':               {'marshal': fields.Raw, 'parser': str},
        'IntField':                 {'marshal': fields.Integer, 'parser': int},
        'LineStringField':          {'marshal': fields.String, 'parser': str},
        'ListField':                {'marshal': fields.List, 'parser': list},
        'LongField':                {'marshal': fields.Float, 'parser': long},
        'MapField':                 {'marshal': fields.Raw, 'parser': str},
        'PointField':               {'marshal': fields.Raw, 'parser': str},
        'PolygonField':             {'marshal': fields.Raw, 'parser': str},
        'ReferenceField':           {'marshal': fields.Raw, 'parser': str},
        'SequenceField':            {'marshal': fields.List, 'parser': list},
        'SortedListField':          {'marshal': fields.List, 'parser': list},
        'URLField':                 {'marshal': fields.String, 'parser': str},
        'UUIDField':                {'marshal': fields.String, 'parser': str},
        'ObjectIdField':            {'marshal': fields.String, 'parser': str}
    })

    def delete(self, **write_concern):
        self._deleted = True
        self.save()

    class Repository(DefaultRepository):
        def __init__(self, outerclass):
            self.document = outerclass

    def getRepository(self):
        return self.Repository(self.__class__)

    @classmethod
    def getMarshal(cls):
        '''
        Static Method to create a dict with information about date should get marshaled when returned

        http://flask-restful.readthedocs.org/en/latest/api.html
        :return:
        '''
        resource_fields = dict()
        for k, v in cls.__dict__.items():
            if isinstance(v, AbstractBaseField):
                resource_fields[k] = cls._type_conversion[v.__class__.__name__]['marshal']
        return resource_fields

    @mongoengine.queryset_manager
    def objects(doc_cls, queryset):
        #queryset = queryset.clone_into(AclAwareQueryset(queryset._document, queryset._collection_obj))
        return queryset.filter(_deleted=False)

        #return doc_cls.Repository(doc_cls).filter_for_acl(queryset)

    @classmethod
    def unmarshal(cls, data, existing = None):
        def parse(obj, data):
            for k, v in data.items():
                field = obj._fields[k]
                if isinstance(field, (mongoengine.ListField)):
                    objects = []
                    for x in v:
                        objects.append(parse(field.field.document_type_obj(), x))
                    setattr(obj, k, objects)
                elif isinstance(field, (mongoengine.EmbeddedDocumentField)):
                    obj_new = field.document_type_obj()
                    setattr(obj, k, parse(obj_new, v))
                elif isinstance(field, (mongoengine.ReferenceField)):
                    obj_new = field.document_type_obj()
                    if 'id' in v:
                        obj_new = obj_new.objects(id=v['id']).first()
                    setattr(obj, k, parse(obj_new, v))
                else:
                    setattr(obj, k, v)
            return obj

        if not existing is None:
            return parse(existing, data)
        return parse(cls(), data)

    @classmethod
    def _set_updated(cls, sender, document, **kwargs):
        document.updated = datetime.datetime.utcnow()