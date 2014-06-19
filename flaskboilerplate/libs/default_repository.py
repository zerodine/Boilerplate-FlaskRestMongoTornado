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

    @check_for_document
    def abortIfNotExists(self, **kwargs):
        """Abort if a document does not exist"""
        doc = self.document.objects(**kwargs).first()
        if doc is None:
            abort(404, message="Document {} doesn't exist".format(kwargs))

        return doc
