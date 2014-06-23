#from mongoengine.queryset.base import BaseQuerySet
from mongoengine.queryset.queryset import QuerySetNoCache, QuerySet
from bson.objectid import ObjectId
from bson.code import Code

class AclAwareQueryset(QuerySetNoCache):

    def check_document_acl(function):
        """Check if a document exists"""
        def decorator(*arg, **kwargs):
            if 'checkAcl' in dir(arg[0]) and arg[0]._document.checkAcl():
                return function(*arg, **kwargs)
            else:
                method = getattr(super(arg[0].__class__, arg[0]), function.__name__)
                if function.__name__ in ['__iter__']:
                    return method()
                return method(*arg, **kwargs)
        return decorator

    @check_document_acl
    def __getitem__(self, key):
        x = super(self.__class__, self).__getitem__(key)
        if isinstance(key, slice):
            return self._iter_with_acl(x)
        elif isinstance(key, int):
            ids = list()
            ids.append(str(x.id))
            ids = self._filter_acl(ids)
            if str(x.id) in ids:
                return x
        raise AttributeError

    @check_document_acl
    def __iter__(self):
        return self._iter_with_acl(self._clone())

    def _clone(self):
        return self.clone_into(QuerySetNoCache(self._document, self._collection_obj))

    def _iter_with_acl(self, iterator):
        ids = list()
        for y in iterator.clone().only('id'):
            ids.append(str(y.id))
        # now take all id's and filter for the allowed ones
        return iterator.clone()(id__in=self._filter_acl(ids))

    @check_document_acl
    def count(self, with_limit_and_skip=True):
        return self._clone().count()

    def _filter_acl(self, ids=list()):
        if len(ids) <= 1:
            return ids
        return ['53a14063c84fd645fb184f29']
