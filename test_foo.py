#!/usr/bin/env python

import unittest
from mock import patch
from lib.foo import foodoo

def milkdud():
    return "gotmilk?"

class TestFoo(unittest.TestCase):

    def test_foodoo(self):
        assert foodoo() == None

    @patch('lib.foo.barnone', milkdud)
    def test_foodoo_withpatch(self):
        assert foodoo() == "gotmilk?"
