from base import BaseTestCase
import time
import json

from datetime import datetime, timedelta

from app.documents.location import Location

class LocationTestCase(BaseTestCase):

    def test_location_occupation(self):
        self.test_location_reservation()
        j = self.test_location_all()
        rv = self.client.post('/location/%s/occupation' % j[0]['id'],
                              data=json.dumps({
                                  "start": datetime.now().isoformat(),
                                  "duration": 60,
                              }),
                              headers=self.headers)
        j = self.parseJsonResponse(rv)
        assert j['rooms'][0]['tables'][0]['seats'][0]['free'] is True
        assert j['rooms'][0]['tables'][0]['seats'][1]['free'] is False

    def test_location_reservation(self):
        j = self.test_location_all()
        location = self.parseJsonResponse(self.client.get('/location/%s' % j[0]['id'], headers=self.headers))
        rv = self.client.post('/location/%s/reservation' % j[0]['id'],
                    data=json.dumps({
                        'start': datetime.now().isoformat(),
                        'end': (datetime.now() + timedelta(hours=2)).isoformat(),
                        'bookable_id': location['rooms'][0]['tables'][0]['seats'][1]['id']
                    }),
                    headers=self.headers
        )
        j = self.parseJsonResponse(rv)
        assert j['status'] == 0
        assert j['location']['name'] == 'Toms little Coffeehouse'
        assert not j['end'] is None and not j['start'] is None
        return j

    def test_location_checkin_occupied(self):
        self.test_location_reservation()

        j = self.test_location_all()
        location = self.parseJsonResponse(self.client.get('/location/%s' % j[0]['id'], headers=self.headers))
        rv = self.client.post('/location/%s/checkin' % j[0]['id'],
                    data=json.dumps({
                        'start': datetime.now().isoformat(),
                        'bookable_id': location['rooms'][0]['tables'][0]['seats'][1]['id']
                    }),
                    headers=self.headers
        )
        j = self.parseJsonResponse(rv)
        assert rv.status_code == 409
        assert 'message' in j and 'type' in j
        assert j['type'] == 'OccupationException'

    def test_location_reservation_occupied(self):
        self.test_location_reservation()

        j = self.test_location_all()
        location = self.parseJsonResponse(self.client.get('/location/%s' % j[0]['id'], headers=self.headers))
        rv = self.client.post('/location/%s/reservation' % j[0]['id'],
                    data=json.dumps({
                        'start': datetime.now().isoformat(),
                        'end': (datetime.now() + timedelta(hours=2)).isoformat(),
                        'bookable_id': location['rooms'][0]['tables'][0]['seats'][1]['id']
                    }),
                    headers=self.headers
        )
        j = self.parseJsonResponse(rv)
        assert rv.status_code == 409
        assert 'message' in j and 'type' in j
        assert j['type'] == 'OccupationException'

    def test_location_checkin(self):
        j = self.test_location_all()
        location = self.parseJsonResponse(self.client.get('/location/%s' % j[0]['id'], headers=self.headers))
        rv = self.client.post('/location/%s/checkin' % j[0]['id'],
                    data=json.dumps({
                        'start': datetime.now().isoformat(),
                        'bookable_id': location['rooms'][0]['tables'][0]['seats'][1]['id']
                    }),
                    headers=self.headers
        )
        j = self.parseJsonResponse(rv)
        assert j['status'] == 0
        assert j['location']['name'] == 'Toms little Coffeehouse'
        assert j['end'] is None
        return j

    def test_location_checkout(self):
        j = self.test_location_checkin()
        rv = self.client.post('/location/checkout/%s' % j['id'],
                              data=json.dumps({
                                  'end': (datetime.now() + timedelta(hours=2)).isoformat()
                              }),
                              headers=self.headers
                              )
        j = self.parseJsonResponse(rv)
        x=1

    def test_location_model_checkin(self):
        start = time.time()
        location = Location.objects().first()
        y = location.rooms[0].tables[0].seats[1]
        booking = Location.checkin(location, bookable=y)
        booking.save()
        location.save()
        self.logInfo("Checkin took %f seconds" % (time.time() - start))

    def test_location_all(self):
        rv = self.client.get('/locations',headers=self.headers)
        j = self.parseJsonResponse(rv)
        assert len(j) is 1
        assert 'name' in j[0].keys()
        return j

    def test_location_get(self):
        j = self.test_location_all()
        rv = self.client.get('/location/%s' % j[0]['id'],headers=self.headers)
        j = self.parseJsonResponse(rv)
        assert 'name' in j.keys()
        assert len(j['rooms'][0]['tables'][0]['seats']) is 2

    def test_location_delete(self):
        j = self.test_location_create()
        rv1 = self.client.delete('/location/%s' % j['id'],headers=self.headers)
        j = self.test_location_all()

    def test_location_put(self):
        j = self.test_location_create()
        rv1 = self.client.put('/location/%s' % j['id'],
                    data=json.dumps({
                        'name': 'Starbucks Basel',
                        'rooms': [
                            {'name': "Room 1"}
                        ]
                    }),
                    follow_redirects=True,
                    headers=self.headers)
        j1 = self.parseJsonResponse(rv1)
        assert 'name' in j1.keys()
        assert j1['name'] == 'Starbucks Basel'
        assert j1['rooms'][0]['name'] == 'Room 1'

    def test_location_stats(self):
        rv = self.client.get('/locationstats',headers=self.headers)
        j = self.parseJsonResponse(rv)
        assert 'count' in j.keys()
        assert j['count'] is 1
        return j

    def test_location_create(self):
        rv1 = self.client.post('/location',
                    data=json.dumps({
                        'name': 'Starbucks Zuerich'
                    }),
                    follow_redirects=True,
                    headers=self.headers)
        rv2 = self.client.get('/locationstats',headers=self.headers)
        j1 = self.parseJsonResponse(rv1)
        j2 = self.parseJsonResponse(rv2)
        assert 'id' in j1.keys()
        assert j2['count'] is 2
        return j1

