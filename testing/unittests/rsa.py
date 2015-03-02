from base import BaseTestCase

class RsaTestCase(BaseTestCase):

    def test_query(self):
        rv = self.client.get('/_rsa')
        #j = self.parseJsonResponse(rv)
