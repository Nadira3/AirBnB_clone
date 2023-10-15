#!/usr/bin/python3
"""
    Test Console Module
"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage


class TestHBNBCommand(unittest.TestCase):
    """ Test Console Function """

    @classmethod
    def setUpClass(cls):
        """ Sets up a test class """
        cls.console = HBNBCommand()

    def setUp(self):
        """ Sets up a test environment """
        self.patcher = patch('sys.stdout', new_callable=StringIO)
        self.mock_stdout = self.patcher.start()

    def tearDown(self):
        """ tear down function """
        self.mock_stdout.close()
        self.patcher.stop()

    def test_create(self):
        """ test create function """
        with patch('builtins.input', side_effect=["create State"]):
            self.console.onecmd("create State")
            output = self.mock_stdout.getvalue().strip()
            self.assertTrue(output)

    def test_show(self):
        """ teest show function """
        with patch('builtins.input', side_effect=["show State 12345"]):
            self.console.onecmd("show State 12345")
            output = self.mock_stdout.getvalue().strip()
            self.assertTrue(output)

    def test_destroy(self):
        """ test destroy function """
        with patch('builtins.input', side_effect=["destroy State 12345"]):
            self.console.onecmd("destroy State 12345")
            output = self.mock_stdout.getvalue().strip()
            self.assertTrue(output)

    def test_all(self):
        """ test all function """
        with patch('builtins.input', side_effect=["all", "all State"]):
            self.console.onecmd("all")
            output_all = self.mock_stdout.getvalue().strip()

            self.console.onecmd("all State")
            output_state = self.mock_stdout.getvalue().strip()

            self.assertTrue(output_all)

    def test_update(self):
        """ test update function """
        with patch('builtins.input',
                   side_effect=["update State 12345 name Texas"]):
            self.console.onecmd("update State 12345 name Texas")
            output = self.mock_stdout.getvalue().strip()
            self.assertTrue(output)

    def test_count(self):
        """ test count function """
        with patch('builtins.input', side_effect=["count State"]):
            self.console.onecmd("count State")
            output = self.mock_stdout.getvalue().strip()
            self.assertTrue(output)

    def test_emptyline(self):
        """ test empty line """
        self.assertEqual(self.console.emptyline(), None)

    def test_help_quit(self):
        """ test help quit """
        self.console.do_help("quit")
        output = self.mock_stdout.getvalue().strip()
        self.assertTrue(output)
