#!/usr/bin/python3
import os
import sys
import unittest
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()
        self.stdout = StringIO()
        self.stderr = StringIO()
        sys.stdout = self.stdout
        sys.stderr = self.stderr

    def tearDown(self):
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

    def test_quit(self):
        self.assertTrue(self.console.onecmd('quit'))

    def test_EOF(self):
        self.assertTrue(self.console.onecmd('EOF'))

    def test_emptyline(self):
        self.assertFalse(self.console.onecmd(''))


if __name__ == '__main__':
    unittest.main():
