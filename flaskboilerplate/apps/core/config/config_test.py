from config import Config as ConfigBase
from ....config.config_test import Config as ConfigTest


class Config(ConfigBase, ConfigTest):
    pass