from flask.ext.script import Manager

from app import create_app
from app.commands import sub_manager

if __name__ == "__main__":
    app = create_app(env='dev')
    manager = Manager(app)
    manager.add_command("core", sub_manager)
    manager.run()