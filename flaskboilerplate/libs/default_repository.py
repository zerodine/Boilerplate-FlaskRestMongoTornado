from flask.ext.restful import abort

class DefaultRepository(object):
    document = None

    def __init__(self, document):
        self.document = document

    def abortIfNotExists(self, **kwargs):
        doc = self.document.objects(**kwargs).first()
        if doc is None:
            abort(404, message="Document {} doesn't exist".format(kwargs))

        return doc