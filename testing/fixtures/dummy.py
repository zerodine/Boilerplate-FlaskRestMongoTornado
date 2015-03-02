__author__ = 'tspycher'

from . import Fixture

class DummyFixtures(Fixture):
    order = 10

    def load(self):
        pass


