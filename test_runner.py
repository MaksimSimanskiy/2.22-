#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import tests

TestSuite = unittest.TestSuite()
TestSuite.addTest(unittest.makeSuite(tests.IndTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(TestSuite)
