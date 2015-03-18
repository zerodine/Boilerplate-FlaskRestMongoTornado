from flask.ext.script import Manager
from flask import current_app
from tests import Tests
from routes import Routes


sub_manager = Manager(current_app)
sub_manager.add_command('test', Tests())
sub_manager.add_command('routes', Routes())
