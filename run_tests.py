#!/usr/bin/env python2

import sys
import unittest
from tests.FuncTests import FuncTests


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(FuncTests),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
