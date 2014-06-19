from flask.ext.script import Manager
from .. import coreApp
from demo import Demo


sub_manager = Manager(coreApp)

# adds a command to the manager
sub_manager.add_command('demo', Demo())
# sub_manager.add_command('anotherCommand', AnotherCommand())