import unittest
from unittest.mock import patch, call
import sys
# sys.path.append('C:\\Users\\Lora\\Documents\\School\\ECE322\\Lab4\\Lab4_src')

sys.path.append('C:\\Users\\lora_\\Documents\\ECE322\\Lab4\\Lab4_src')

from unittest.mock import Mock
from unittest.mock import patch

from modules.ModuleF import ModuleF

class TestModuleF(unittest.TestCase):  
    def setUp(self):
        self.modF = Mock()
        self.modF = ModuleF()

    @patch('builtins.print')
    def test_displayData(self, mockPrint):
        data = [
            'one',
            'two',
            'three'
        ]
        self.modF.displayData(data)
        calls = [
            call("Current Data:"),
            call("----------------------------------------------------------"),
            call("1 one"),
            call("2 two"),
            call("3 three"),
            call("----------------------------------------------------------")
        ]
        mockPrint.assert_has_calls(calls)

if __name__ == '__main__':
    unittest.main()
