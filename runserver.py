#import logging
import argparse
from flaskboilerplate import create_app
from werkzeug._internal import _log

# for tornado integration
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Staring Flask based RESTful Server')
    parser.add_argument('port', metavar='Port', type=int, nargs='?', default=5000,
                       help='port to run the application')
    parser.add_argument('--env', '-e', dest='environment', action='store',
                   default='dev',
                   help='type of environment')
    parser.add_argument('--tornado', '-t', dest='tornado', action='store_true', help='run the server as tornado wsgi')
    args = parser.parse_args()

    app = create_app()

    if args.environment == 'dev' or args.environment == 'test':
        app.debug = True
    else:
        pass

    if args.tornado:
        try:
            _log('info', " * Starting Tornado Server")
            http_server = HTTPServer(WSGIContainer(app))
            http_server.listen(args.port)
            IOLoop.instance().start()
        except KeyboardInterrupt as e:
            _log('info', " * Stopping Tornado Server by Ctrl+C")

    else:
        _log('info', " * Starting Flask Internal (dev) Server")
        app.run(port=args.port)
        _log('info', " * Stopping Flask Internal (dev) Server")
