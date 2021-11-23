import unittest
import sys
# sys.path.append('C:\\Users\\Lora\\Documents\\School\\ECE322\\Lab4\\Lab4_src')

sys.path.append('C:\\Users\\lora_\\Documents\\ECE322\\Lab4\\Lab4_src')


from io import StringIO

from unittest.mock import Mock
from unittest.mock import patch
from unittest.mock import mock_open

from modules.ModuleB import ModuleB

### change code

class TestModuleB(unittest.TestCase):
    def setUp(self):
        self.modF = Mock()  
        self.modB = ModuleB(self.modF)

    @patch('builtins.open', new_callable=mock_open,
        read_data = "one, 1\n"
                    "two, 2\n"
                    "too, many, 2\n"
                    "three, 3\n"
                    "four\n"
                    "five, 5\n"
                    )
    def test_loadFile(self, mockFile):
        data = self.modB.loadFile('fileName.txt')
        self.assertEqual(4, len(data))
        mockFile.assert_called_once_with('fileName.txt')
        self.modF.displayData.assert_called_once_with(data)
        mockFile().__exit__.assert_called()

    def test_FGetter(self):
        self.modB._f = "Hello"
        self.assertEqual(self.modB.f, "Hello")

    def test_FSetter(self):
        self.modB.f = "Hello"
        self.assertEqual(self.modB._f, "Hello")

    @patch('builtins.print')
    @patch('builtins.open')
    def test_IOError(self, mockFile, mockPrint):
        error = IOError()
        error.filename = 'fileName.txt'
        mockFile.side_effect = error
        data = self.modB.loadFile('fileName.txt')
        mockFile.assert_called_once_with('fileName.txt')
        self.modF.displayData.assert_called_once_with(data)
        mockPrint.assert_called_once_with("Could not read file:fileName.txt")

if __name__ == '__main__':
    unittest.main()
