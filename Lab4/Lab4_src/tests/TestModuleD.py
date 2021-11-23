import unittest
import sys
# sys.path.append('C:\\Users\\Lora\\Documents\\School\\ECE322\\Lab4\\Lab4_src')

sys.path.append('C:\\Users\\lora_\\Documents\\ECE322\\Lab4\\Lab4_src')

from unittest.mock import Mock
from modules.ModuleD import ModuleD

### change code
class TestModuleD(unittest.TestCase):
    def setUp(self):
        self.modF = Mock()
        self.modG = Mock()
        self.modD = ModuleD(self.modF, self.modG)

    def test_insertData(self):
        data = [
            ('A', '1'),
            ('B', '2'),
            ('C', '3'),
            ('D', '4'),
        ]

        result = self.modD.insertData(data, 'E', '5', 'fileName.txt')
        self.assertEqual(len(result), 5)
        self.modF.displayData.assert_called_once_with(data=data)
        self.modG.updateData.assert_called_once_with('fileName.txt', data)

    def test_FGetter(self):
        self.modD._f = "Hello"
        self.assertEqual(self.modD.f, "Hello")

    def test_FSetter(self):
        self.modD.f = "Hello"
        self.assertEqual(self.modD._f, "Hello")

if __name__ == '__main__':
    unittest.main()
