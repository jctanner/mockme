#!/usr/bin/env python

import unittest
from mock import patch
from lib.foo import foodoo

class TestFoo(unittest.TestCase):

    def test_foodoo(self):
        assert foodoo() == None

    # make this pass!
    def test_foodoo_withpatch(self):
        assert foodoo() == "gotmilk?"
