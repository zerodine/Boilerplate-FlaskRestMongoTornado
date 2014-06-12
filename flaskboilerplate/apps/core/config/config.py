class Config(object):
    MONGODB_SETTINGS = dict({
        "DB": "flaskdemo",
        #"USERNAME": "my_user_name",
        #"PASSWORD": "my_secret_password",
        "HOST": "localhost",
        "PORT": 27017,
        #"DEBUG_TB_PANELS": "flask.ext.mongoengine.panels.MongoDebugPanel"
    })

