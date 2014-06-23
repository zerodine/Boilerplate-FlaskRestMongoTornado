from config import Config as ConfigBase


class Config(ConfigBase):
    DEBUG = True
    TESTING = True

    MONGODB_SETTINGS = dict({
        "DB": "flaskdemo_test",
        "HOST": "localhost",
        "PORT": 27017,
    })