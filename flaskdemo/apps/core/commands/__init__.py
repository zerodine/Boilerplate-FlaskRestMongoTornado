from flask.ext.script import Manager
from flaskdemo.apps import coreApp

from demo import Demo

sub_manager = Manager(coreApp)
sub_manager.add_command('demo', Demo())
