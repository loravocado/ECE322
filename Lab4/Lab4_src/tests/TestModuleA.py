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
        self.modB = Mock()
        self.modC = Mock()
        self.modD = Mock()
        self.modE = Mock()
        
        self.modA = ModuleA(self.modB, self.modC, self.modD, self.modE)
        self.modA._data = ["Jane", "Doe"]

    @patch('builtins.print')
    def test_help(self, print_mock):
        self.assertEqual(self.modA.displayHelp(), True)
        print_mock.assert_called_once_with(
            "Available Commands: \n"
            "load <filepath>\n"
            "add <name> <number>\n"
            "update <index> <name> <number>\n"
            "delete <index>\n"
            "sort\n"
            "exit"
        )
    
    def test_parseDeleteWithoutValue(self):
        self.modD.deleteData.return_value = None
        self.modA._filename = "testFile"
        self.assertEqual(self.modA.parseDelete(1), False)
        self.modD.deleteData.assert_called_once()

    def test_parseDeleteWithValue(self):
        self.modD.deleteData.return_value = ["Jane"]
        self.modA._filename = "testFile"
        self.assertEqual(self.modA.parseDelete(1), True)
        self.modD.deleteData.assert_called_once()

    def test_parseLoadData(self):
        self.modB.loadFile.return_value = ["Jane"]
        self.assertEqual(self.modA.parseLoad("testFilename.txt"), True)
        self.modB.loadFile.assert_called_once()

    def test_parseLoadNoData(self):
        self.modB.loadFile.return_value = None
        self.assertEqual(self.modA.parseLoad("testFilename.txt"), False)
        self.modB.loadFile.assert_called_once()

    def test_parseAddWithData(self):
        self.modD.insertData.return_value = ["Jane"]
        self.modA._filename = "testFile"
        self.assertEqual(self.modA.parseAdd("John", "1"), True)
        self.modD.insertData.assert_called_once()

    def test_parseAddWithNoData(self):
        self.modD.insertData.return_value = None
        self.modA._filename = "testFile"
        self.assertEqual(self.modA.parseAdd("John", "1"), False)
        self.modD.insertData.assert_called_once()

    def test_runSortWithData(self):
        self.modC.sortData.return_value = ["Jane"]
        self.assertEqual(self.modA.runSort(), True)
        self.modC.sortData.assert_called_once()
        
    def test_runSortWithNoData(self):
        self.modC.sortData.return_value = None
        self.assertEqual(self.modA.runSort(), False)
        self.modC.sortData.assert_called_once()

    def test_parseUpdateWithData(self):
        self.modD.updateData.return_value = ["Data"]
        self.modA._filename = "testFile"
        self.assertEqual(self.modA.parseUpdate(1, "John", "1"), True)
        self.modD.updateData.assert_called_once()
    
    def test_parseUpdateWithNoData(self):
        self.modD.updateData.return_value = None
        self.modA._filename = "testFile"
        self.assertEqual(self.modA.parseUpdate(1, "John", "1"), False)
        self.modD.updateData.assert_called_once()

    def test_runExit(self):
        with self.assertRaises(SystemExit) as cm:
            self.modA.runExit()
            self.assertEqual(cm.exception.code, 1)
            
    def test_dataGetter(self):
        self.modA._data = "John"
        self.assertEqual(self.modA.data, "John")

    def test_dataSetter(self):
        self.modA.data = "testdata"
        self.assertEqual(self.modA._f, "testdata")

    @patch('builtins.print')
    def test_unknownCmd(self, mockPrint):
        self.modA.run("")
        mockPrint.assert_called_with("Unknown command, type 'help' for command list.")

    @patch('builtins.print')
    def test_noCommand(self, mockPrint):
        self.modA.run()
        mockPrint.assert_called_with("No command passed!")
    
    @patch('builtins.print')
    def test_allCommands(self, mockPrint):
        self.modA.displayHelp = Mock()
        self.modA.parseLoad = Mock()
        self.modA.parseAdd = Mock()
        self.modA.runSort = Mock()
        self.modA.parseUpdate = Mock()
        self.modA.parseDelete = Mock()
        self.modA.runExit = Mock()

        self.modA.run()
        mockPrint.assert_called_with("No command passed!")

        self.modA.run("beep")
        mockPrint.assert_called_with("Unknown command, type 'help' for command list.")

        self.modA.run("help")
        self.modA.displayHelp.assert_called_once()

        self.modA.run("load", "testFilename.txt")
        self.modA.parseLoad.assert_called_once()

        self.modA.run("update", 1, "John", "1")
        self.modA.parseUpdate.assert_called_once()
        
        self.modA.run("add", "John", "1")
        self.modA.parseAdd.assert_called_once()

        self.modA.run("delete", 1)
        self.modA.parseDelete.assert_called_once()

        self.modA.run("sort")
        self.modA.runSort.assert_called_once()

        self.modA.runExit()
        self.modA.runExit.assert_called_once()

if __name__ == '__main__':
    unittest.main()
