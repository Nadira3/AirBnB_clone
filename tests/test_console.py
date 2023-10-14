import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage


class TestHBNBCommand(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.console = HBNBCommand()

    def setUp(self):
        self.patcher = patch('sys.stdout', new_callable=StringIO)
        self.mock_stdout = self.patcher.start()

    def tearDown(self):
        self.mock_stdout.close()
        self.patcher.stop()

    def test_create(self):
        with patch('builtins.input', side_effect=["create State"]):
            self.console.onecmd("create State")
            output = self.mock_stdout.getvalue().strip()
            self.assertTrue(output)

    def test_show(self):
        with patch('builtins.input', side_effect=["show State 12345"]):
            self.console.onecmd("show State 12345")
            output = self.mock_stdout.getvalue().strip()
            self.assertTrue(output)

    def test_destroy(self):
        with patch('builtins.input', side_effect=["destroy State 12345"]):
            self.console.onecmd("destroy State 12345")
            output = self.mock_stdout.getvalue().strip()
            self.assertTrue(output)

    def test_all(self):
        with patch('builtins.input', side_effect=["all", "all State"]):
            self.console.onecmd("all")
            output_all = self.mock_stdout.getvalue().strip()

            self.console.onecmd("all State")
            output_state = self.mock_stdout.getvalue().strip()

            self.assertTrue(output_all)

    def test_update(self):
        with patch('builtins.input',
                   side_effect=["update State 12345 name Texas"]):
            self.console.onecmd("update State 12345 name Texas")
            output = self.mock_stdout.getvalue().strip()
            self.assertTrue(output)

    def test_count(self):
        with patch('builtins.input', side_effect=["count State"]):
            self.console.onecmd("count State")
            output = self.mock_stdout.getvalue().strip()
            self.assertTrue(output)

    def test_emptyline(self):
        self.assertEqual(self.console.emptyline(), None)

    def test_help_quit(self):
        self.console.do_help("quit")
        output = self.mock_stdout.getvalue().strip()
        self.assertTrue(output)
