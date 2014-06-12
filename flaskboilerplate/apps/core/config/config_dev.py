from config import Config as ConfigBase
from ....config.config_dev import Config as ConfigDev


class Config(ConfigBase, ConfigDev):
    pass