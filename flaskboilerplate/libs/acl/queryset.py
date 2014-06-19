#from mongoengine.queryset.base import BaseQuerySet
from mongoengine.queryset.queryset import QuerySetNoCache, QuerySet
from bson.objectid import ObjectId
from bson.code import Code

class AclAwareQueryset(QuerySet):

    def __getitem__(self, key):
        x = super(self.__class__, self).__getitem__(key)
        ids = list()
        ids.append(str(x.id))
        ids = self._filter_acl(ids)
        if str(x.id) in ids:
            return x
        return None

    def __iter__(self):
        x = super(self.__class__, self).__iter__()
        ids = list()
        objs = list()
        for y in x:
            ids.append(str(y.id))
            objs.append(y)
        ids = self._filter_acl(ids)
        for y in objs:
            if str(y.id) in ids:
                yield y

    def _filter_acl(self, ids = list()):
        if len(ids) <= 1:
            return ids
        deleted = False
        for x in ids:
            if deleted:
                deleted = False
                continue
            deleted = True
            ids.remove(x)
        return ids

    #@property
    #def _cursor(self):
    #    if self._cursor_obj is None:
    #
    #        self._cursor_obj = super(self.__class__, self)._cursor
    #        q = str(u'{"_id": {"$in": ["53a14063c84fd645fb184f2a"]}}')
    #        self._cursor_obj.where(q)
    #
    #        #c = Code({"_id": {"$in": [ObjectId("53a14063c84fd645fb184f2a")]}})
    #        print "afasdf"
    #
    #    return self._cursor_obj
