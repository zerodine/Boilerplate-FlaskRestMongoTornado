import os, json
from flask import current_app
#from app.odm import odm
import unittest
import tempfile
#from mongoengine.connection import _get_db

from testing.fixtures import loadFixtures
from werkzeug._internal import _log


class BaseTestCase(unittest.TestCase):

    headers = [('Content-Type', 'application/json')]

    def logInfo(self, message):
        _log('info', message)

    def __init__(self, methodName='runTest'):
        super(BaseTestCase, self).__init__(methodName)

    def setUp(self):
        self.db_fd, current_app.config['DATABASE'] = tempfile.mkstemp()
        current_app.config['TESTING'] = True
        self.client = current_app.test_client()
        #db = _get_db()
        #db.connection.drop_database(current_app.config['MONGODB_SETTINGS']['DB'])
        loadFixtures()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(current_app.config['DATABASE'])

    def parseJsonResponse(self, rv):
        return json.loads(rv.data)
