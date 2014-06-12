from config import Config as ConfigBase
from flaskdemo.config.config_test import Config as ConfigTest


class Config(ConfigBase, ConfigTest):
    pass