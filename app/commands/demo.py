from flask.ext.script import Command

class Demo(Command):
    """
        prints hello world
    """

    def run(self):
        """Just prints a hello world"""
        print "hello world"

