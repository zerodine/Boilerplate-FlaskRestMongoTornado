from config import Config as ConfigBase
from flaskboilerplate.config.config_prod import Config as ConfigProd


class Config(ConfigBase, ConfigProd):
    pass