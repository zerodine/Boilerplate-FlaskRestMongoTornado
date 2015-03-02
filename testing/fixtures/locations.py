__author__ = 'tspycher'

from . import Fixture
from app.documents.location import Location,Room,Table,Seat

class LocationsFixtures(Fixture):
    order = 1

    def load(self):
        def createSeats(num):
            x = []
            for i in range(num):
                x.append(Seat(name="Seat %d" % i))
            return x

        Location(name="Toms little Coffeehouse",
            rooms=[
                Room(name="Haupt Saal", isBookable=False,  tables=[
                    Table(name="Demotisch", isBookable=False, seats=createSeats(2))
                ])
            ]).save()

