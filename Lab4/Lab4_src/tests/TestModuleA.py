import unittest
import sys
# sys.path.append('C:\\Users\\Lora\\Documents\\School\\ECE322\\Lab4\\Lab4_src')

sys.path.append('C:\\Users\\lora_\\Documents\\ECE322\\Lab4\\Lab4_src')


from io import StringIO

from unittest.mock import Mock
from unittest.mock import patch

from modules.ModuleA import ModuleA

### change code

class TestModuleA(unittest.TestCase):
    def setUp(self):
        self.b = Mock()
        self.c = Mock()
        self.d = Mock()
        self.e = Mock()
        self.a = ModuleA(self.b, self.c, self.d, self.e)
        self.a._data = ["a", "b"]

    def test_parse_delete_with_data(self):
        self.d.deleteData.return_value = ["a"]
        self.a._filename = 'fakefile'

        result = self.a.parseDelete(1)

        self.assertEqual(result, True)
        self.d.deleteData.assert_called_once_with(["a", "b"], 1, 'fakefile')

    def test_parse_delete_without_data(self):
        self.d.deleteData.return_value = None
        self.a._filename = 'fakefile'

        result = self.a.parseDelete(1)

        self.assertEqual(result, False)
        self.d.deleteData.assert_called_once_with(["a", "b"], 1, 'fakefile')

    @patch('builtins.print')
    def test_display_help(self, print_mock):
        result = self.a.displayHelp()

        self.assertEqual(result, True)
        print_mock.assert_called_once_with(
            "Available Commands: \n"
            "load <filepath>\n"
            "add <name> <number>\n"
            "update <index> <name> <number>\n"
            "delete <index>\n"
            "sort\n"
            "exit"
        )

    def test_parse_load_with_data(self):
        self.b.loadFile.return_value = []
        result = self.a.parseLoad('fakefile')

        self.assertEqual(result, True)
        self.b.loadFile.assert_called_once_with('fakefile')

    def test_parse_load_without_data(self):
        self.b.loadFile.return_value = None
        result = self.a.parseLoad('fakefile')

        self.assertEqual(result, False)
        self.b.loadFile.assert_called_once_with('fakefile')

    def test_parse_add_with_data(self):
        self.d.insertData.return_value = ["a"]
        self.a._filename = 'fakefile'

        result = self.a.parseAdd('fakename', '23')

        self.assertEqual(result, True)
        self.d.insertData.assert_called_once_with(["a", "b"], 'fakename', '23', 'fakefile')

    def test_parse_add_without_data(self):
        self.d.insertData.return_value = None
        self.a._filename = 'fakefile'

        result = self.a.parseAdd('fakename', '23')

        self.assertEqual(result, False)
        self.d.insertData.assert_called_once_with(["a", "b"], 'fakename', '23', 'fakefile')

    def test_run_sort_with_data(self):
        self.c.sortData.return_value = ["a"]

        result = self.a.runSort()

        self.assertEqual(result, True)
        self.c.sortData.assert_called_once_with(["a", "b"])

    def test_run_sort_without_data(self):
        self.c.sortData.return_value = None

        result = self.a.runSort()

        self.assertEqual(result, False)
        self.c.sortData.assert_called_once_with(["a", "b"])

    def test_parse_update_with_data(self):
        self.d.updateData.return_value = ["a"]
        self.a._filename = 'fakefile'

        result = self.a.parseUpdate(1, 'fakename', '23')

        self.assertEqual(result, True)
        self.d.updateData.assert_called_once_with(["a", "b"], 1, 'fakename', '23', 'fakefile')

    def test_parse_update_without_data(self):
        self.d.updateData.return_value = None
        self.a._filename = 'fakefile'

        result = self.a.parseUpdate(1, 'fakename', '23')

        self.assertEqual(result, False)
        self.d.updateData.assert_called_once_with(["a", "b"], 1, 'fakename', '23', 'fakefile')

    def test_run_exit(self):
        self.a.runExit()
        self.e.exitProgram.assert_called_once()

    def test_data_getter(self):
        self.a._data = "testdata"
        self.assertEqual(self.a.data, "testdata")

    def test_data_setter(self):
        self.a.data = "testdata"
        self.assertEqual(self.a._data, "testdata")

    @patch('builtins.print')
    def test_no_command(self, print_mock):
        self.a.run()
        print_mock.assert_called_with("No command passed!")

    @patch('builtins.print')
    def test_no_file_loaded_all_cmds(self, print_mock):
        self.a._data = None

        # Stub all function calls
        self.a.displayHelp = Mock()
        self.a.parseLoad = Mock()
        self.a.parseAdd = Mock()
        self.a.runSort = Mock()
        self.a.parseUpdate = Mock()
        self.a.parseDelete = Mock()
        self.a.runExit = Mock()

        # Set up array of tuples of commands to execute
        # Structure is: (command, should_fail, mock)
        # where command is the command to pass to ModuleA.run()
        # and should_fail is a flag to check if the call should fail for no data
        # and mock is the mock object of the function to check
        commands = [
            ("help", False, self.a.displayHelp),
            ("load", False, self.a.parseLoad),
            ("add", True, self.a.parseAdd),
            ("sort", True, self.a.runSort),
            ("update", True, self.a.parseUpdate),
            ("delete", True, self.a.parseDelete),
            ("exit", False, self.a.runExit),
        ]

        # Run each command
        for command, should_fail, mock in commands:
            print_mock.reset_mock()
            self.a.run(command, "arg1", "arg2", "arg3") # Add generic args so we don't throw any IndexErrors
            if should_fail:
                mock.assert_not_called()
                print_mock.assert_called_with("No file loaded!")
            else:
                mock.assert_called()

    @patch('builtins.print')
    def test_bad_arg_count_all_cmds(self, print_mock):
        # Stub all function calls
        self.a.displayHelp = Mock()
        self.a.parseLoad = Mock()
        self.a.parseAdd = Mock()
        self.a.runSort = Mock()
        self.a.parseUpdate = Mock()
        self.a.parseDelete = Mock()
        self.a.runExit = Mock()

        # Set up array of tuples of commands to execute
        # Structure is: (command, should_fail, mock)
        # where command is the command to pass to ModuleA.run()
        # and should_fail is a flag to check if the call should fail for no data
        # and mock is the mock object of the function to check
        commands = [
            ("help", False, self.a.displayHelp),
            ("load", True, self.a.parseLoad),
            ("add", True, self.a.parseAdd),
            ("sort", False, self.a.runSort),
            ("update", True, self.a.parseUpdate),
            ("delete", True, self.a.parseDelete),
            ("exit", False, self.a.runExit),
        ]

        # Run each command
        for command, should_fail, mock in commands:
            print_mock.reset_mock()
            self.a.run(command)  # Add generic args so we don't throw any IndexErrors
            if should_fail:
                mock.assert_not_called()
                print_mock.assert_called_with("Malformed command!")
            else:
                mock.assert_called()

    @patch('builtins.print')
    def test_unknown_cmd(self, print_mock):
        self.a.run("sudo make_me_a_sandwhich")
        print_mock.assert_called_with("Unknown command, type 'help' for command list.")

    @patch('builtins.print')
    def test_all_cmds(self, print_mock):
        # Stub all function calls
        self.a.displayHelp = Mock()
        self.a.parseLoad = Mock()
        self.a.parseAdd = Mock()
        self.a.runSort = Mock()
        self.a.parseUpdate = Mock()
        self.a.parseDelete = Mock()
        self.a.runExit = Mock()

        # Set up array of tuples of commands to execute
        # Structure is: (command, num_args, mock)
        # where command is the command to pass to ModuleA.run()
        # and num_args is how many args should have been passed in
        # and mock is the mock object of the function to check
        commands = [
            ("help", 0, self.a.displayHelp),
            ("load", 1, self.a.parseLoad),
            ("add", 2, self.a.parseAdd),
            ("sort", 0, self.a.runSort),
            ("update", 3, self.a.parseUpdate),
            ("delete", 1, self.a.parseDelete),
            ("exit", 0, self.a.runExit),
        ]

        # Run each command
        for command, num_args, mock in commands:
            print_mock.reset_mock()
            self.a.run(command, "arg1", "arg2", "arg3")  # Add generic args to check for
            if num_args == 0:
                mock.assert_called_once()
            elif num_args == 1:
                mock.assert_called_once_with("arg1")
            elif num_args == 2:
                mock.assert_called_once_with("arg1", "arg2")
            elif num_args == 3:
                mock.assert_called_once_with("arg1", "arg2", "arg3")
if __name__ == '__main__':
    unittest.main()
