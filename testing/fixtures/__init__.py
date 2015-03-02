__author__ = 'tspycher'

def loadFixtures():
    from dummy import DummyFixtures
    from locations import LocationsFixtures
    from mongoengine.connection import _get_db
    from flask import current_app

    # Clear Database before createing data in it
    #db_fd, current_app.config['DATABASE'] = tempfile.mkstemp()
    #current_app.config['TESTING'] = True
    #client = current_app.test_client()
    db = _get_db()
    db.connection.drop_database(current_app.config['MONGODB_SETTINGS']['DB'])

    fixtures = [DummyFixtures(), LocationsFixtures()]
    for fixture in sorted(fixtures, key=lambda f: f.order):
        fixture.load()

class Fixture(object):
    order = 0

    def getOrder(self):
        return self.order

    def load(self):
        raise NotImplemented()