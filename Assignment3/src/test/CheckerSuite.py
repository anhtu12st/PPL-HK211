import sys
import unittest
from TestUtils import TestChecker

if not './main/bkool/parser/' in sys.path:
    from main.bkool.utils.AST import *
else:
    from AST import *

class CheckerSuite(unittest.TestCase):

    def test0(self):
        input = """
        class XXX { }
        class XXX { }
        """
        expect = "Redeclared Class: XXX"
        self.assertTrue(TestChecker.test(input, expect, 400))
    