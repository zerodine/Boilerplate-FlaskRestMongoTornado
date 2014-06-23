#import logging
import argparse
import os
from app import create_app
from werkzeug._internal import _log
from app.libs import Rsa

# For tornado integration
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop


if __name__ == "__main__":
    # CLI arguments
    parser = argparse.ArgumentParser(description='Staring Flask based RESTful Server')
    parser.add_argument('port', metavar='Port', type=int, nargs='?', default=5000, help='port to run the application')
    parser.add_argument('--env', '-e', dest='environment', action='store', default='dev', help='type of environment')
    parser.add_argument('--tornado', '-t', dest='tornado', action='store_true', help='run the server as tornado wsgi')
    parser.add_argument('--ssl', '-s', dest='use_ssl', action='store_true', help='run server with ssl certs')
    parser.add_argument('--ssl-certfile', '-c', dest='ssl_certfile', action='store', default='server.crt', help='ssl certificate file')
    parser.add_argument('--ssl-keyfile', '-k', dest='ssl_keyfile', action='store', default='server.key', help='ssl key file')
    parser.add_argument('--rsa-create', '-r', dest='creatersa', action='store_true', help='create rsa keymaterial and store it in --rsa-pubfile and --rsa-privfile')
    parser.add_argument('--rsa-pubfile', '-p', dest='rsa_pubfile', action='store', help='filename of the rsa public key file', default="rsa.pub")
    parser.add_argument('--rsa-privfile', '-q', dest='rsa_privfile', action='store', help='filename of the rsa private key file', default="rsa.priv")
    args = parser.parse_args()

    # Generate a rsa object
    rsa = None
    if args.creatersa:
        rsa = Rsa()
        rsa.createKeypair()
        Rsa.storeKey(args.rsa_pubfile, rsa.dumpKeys()[0])
        Rsa.storeKey(args.rsa_privfile, rsa.dumpKeys()[1])

    elif args.rsa_pubfile:
        rsa = Rsa()
        publicKey = Rsa.loadKey(args.rsa_pubfile)
        privateKey = Rsa.loadKey(args.rsa_privfile)
        if publicKey:
            rsa.loadKeypair(publicKey, privateKey)

    # Create the app
    app = create_app(env=args.environment, services={'rsa': rsa})

    if args.environment == 'dev' or args.environment == 'test':
        pass
    else:
        pass

    # Start app in tornado wsgi container
    if args.tornado:
        try:
            _log('info', " * Starting Tornado Server")
            if args.use_ssl:
                ssl_options={'certfile': os.path.join(args.ssl_certfile), 'keyfile': os.path.join(args.ssl_keyfile)}
            else:
                ssl_options=None
            http_server = HTTPServer(WSGIContainer(app), ssl_options=ssl_options)
            http_server.listen(args.port)
            IOLoop.instance().start()
        except KeyboardInterrupt as e:
            _log('info', " * Stopping Tornado Server by Ctrl+C")
    else:
        _log('info', " * Starting Flask Internal (dev) Server")
        app.run(port=args.port)
        _log('info', " * Stopping Flask Internal (dev) Server")
