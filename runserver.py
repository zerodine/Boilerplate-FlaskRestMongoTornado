from flaskboilerplate import app

# for tornado integration
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

# the toolbar is only enabled in debug mode:
app.debug = True
# toolbar = DebugToolbarExtension(coreApp)

# start with Flask
#app.run(debug=True)

# start with Tornado
http_server = HTTPServer(WSGIContainer(app))
http_server.listen(5000)
IOLoop.instance().start()