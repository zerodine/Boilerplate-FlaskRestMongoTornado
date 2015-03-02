__author__ = 'tspycher'

from flask.ext.restful import reqparse
import dateutil.parser

class PlainEntity(dict):

    @staticmethod
    def from_utc(utcTime, *args, **kwargs):
        """
        Convert UTC time string to time.struct_time
        """
        return  dateutil.parser.parse(utcTime)

    def __getattribute__(self, item):
        return self[item]

    @classmethod
    def parseRequest(cls):
        parser = reqparse.RequestParser(namespace_class=cls)
        for a,v in cls.__dict__.items():
            if isinstance(v, (reqparse.Argument)):
                parser.add_argument(v)
        return parser.parse_args()
