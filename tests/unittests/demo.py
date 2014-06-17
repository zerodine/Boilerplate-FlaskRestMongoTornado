import unittest
from base import BaseTestCase


class DemoTestCase(BaseTestCase):

    def test_demo(self):
        rv = self.client.get('/demo1')
        assert 'Hello World!' in rv.data

if __name__ == '__main__':
    unittest.main()