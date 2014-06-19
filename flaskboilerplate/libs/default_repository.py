from flask.ext.restful import abort

class DefaultRepository(object):
    document = None

    def check_for_document(function):
        """Check if a document exists"""
        def decorator(*arg, **kwargs):
            if arg[0].document is None:
                abort(500,
                      message="Internal Server Error",
                      description="repository document attribute is None, which should not be the case"
                )
            return function(*arg, **kwargs)
        return decorator

    #def filter_for_acl(function):
    #    def decorator(*arg, **kwargs):
    #        data = function(*arg, **kwargs)
    #        for d in data:
    #            pass
    #        return data
    #    return decorator

    def filter_for_acl(self, queryset):
        bulkaclids = list()
        classname = None
        querysetcopy = queryset
        for d in querysetcopy.only('id'):
            if classname is None:
                classname = d.__class__.__name__
            bulkaclids.append(str(d.id))
        bulkacl = self._query_acl({classname: bulkaclids})
        return queryset(id__in=bulkacl[classname])


    def _query_acl(self, bulkacl):
        odd = True
        for classname, ids in bulkacl.iteritems():
            for id in ids:
                if odd:
                    odd = False
                    continue
                odd = True
                bulkacl[classname].remove(id)

        return bulkacl


    @check_for_document
    def abortIfNotExists(self, **kwargs):
        """Abort if a document does not exist"""
        doc = self.document.objects(**kwargs).first()
        if doc is None:
            abort(404, message="Document {} doesn't exist".format(kwargs))

        return doc
