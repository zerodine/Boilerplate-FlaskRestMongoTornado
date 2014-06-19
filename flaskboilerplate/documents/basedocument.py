from . import odm as db
from ..libs import DefaultRepository
from mongoengine import signals, queryset_manager


class Basedocument(db.Document):
    meta = {'abstract': True}

    class Repository(DefaultRepository):
        def __init__(self, outerclass):
            self.document = outerclass

    def getRepository(self):
        return self.Repository(self.__class__)

    @queryset_manager
    def objects(doc_cls, queryset):
        return doc_cls.Repository(doc_cls).filter_for_acl(queryset)