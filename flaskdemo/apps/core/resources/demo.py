from flask.ext import restful

class Demo(restful.Resource):
    def get(self):
        return {'hello': 'world'}
