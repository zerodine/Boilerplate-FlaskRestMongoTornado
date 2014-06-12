import os


env = os.getenv('APP_ENV', 'dev')

if env == 'dev':
    from config_dev import Config
elif env == 'test':
    from config_test import Config
elif env == 'prod':
    from config_prod import Config