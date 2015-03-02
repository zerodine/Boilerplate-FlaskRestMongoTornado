__author__ = 'tspycher'

from flask.ext.script import Command, Option
import unittest, os
import xmlrunner
from testing.unittests import getTests

class Tests(Command):
    """
        Runs all tests
    """

    option_list = (
        Option('--xml', '-x', dest='xml', action='store_true'),
    )

    def run(self, xml=False):
        """Just prints a hello world"""
        suite = self.suite()
        if not xml:
            unittest.TextTestRunner(verbosity=2).run(suite)
        else:
            xmlrunner.XMLTestRunner(output='./metrics/tests/').run(suite)

    def suite(self):
        loader = unittest.TestLoader()

        cases_list = []
        for test_class in getTests():
            case = loader.loadTestsFromTestCase(test_class)
            cases_list.append(case)

        suite = unittest.TestSuite(cases_list)
        return suite


