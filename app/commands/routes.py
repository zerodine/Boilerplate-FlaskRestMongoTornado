__author__ = 'tspycher'

from flask.ext.script import Command
from flask import current_app

class Routes(Command):
    """
        Lists all Routes
    """

    def run(self):
        routes_title = ['URL', 'METHOD', 'ENDPOINT']
        routes = []
        for rule in current_app.url_map.iter_rules():
            routes.append((rule.rule, ",".join(rule.methods), rule.endpoint))

        row_format = "{:>2}{:<55}{:>25}{:>35}"
        print row_format.format("", *routes_title)
        print "-" * len(row_format.format("", *routes_title))
        for row in routes:
            print row_format.format("", *row)