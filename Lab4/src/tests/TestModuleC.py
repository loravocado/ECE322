import unittest
import sys
# sys.path.append('C:\\Users\\Lora\\Documents\\School\\ECE322\\Lab4\\Lab4_src')

sys.path.append('C:\\Users\\lora_\\Documents\\ECE322\\Lab4\\Lab4_src')

from io import StringIO

from unittest.mock import Mock
from unittest.mock import patch
from unittest.mock import mock_open

from modules.ModuleC import ModuleC
from data.Entry import Entry

### change code

class TestModuleC(unittest.TestCase):
    def setUp(self):
        self.modF = Mock()
        self.modC = ModuleC(self.modF)

    def test_sortData(self):
        data = [
            Entry('C', '3'),
            Entry('D', '4'),
            Entry('A', '1'),
            Entry('B', '2'),
        ]
        expected = [
            ('A', '1'),
            ('B', '2'),
            ('C', '3'),
            ('D', '4'),
        ]
        result = self.modC.sortData(data)
        for i in range(len(result)):
            self.assertEqual(result[i].name, expected[i][0])
            self.assertEqual(result[i].number, expected[i][1])
        self.modF.displayData.assert_called_once_with(result)

    def test_FGetter(self):
        self.modC._f = "Hello"
        self.assertEqual(self.modC.f, "Hello")

    def test_FSetter(self):
        self.modC.f = "Hello"
        self.assertEqual(self.modC._f, "Hello")

if __name__ == '__main__':
    unittest.main()
