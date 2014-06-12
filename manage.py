from flask.ext.script import Manager

def sub_opts(*app, **kwargs):
    pass

manager = Manager(sub_opts)

from flaskdemo.apps.core.commands import sub_manager as core_sub_manager
manager.add_command("core", core_sub_manager)

if __name__ == "__main__":
    manager.run()