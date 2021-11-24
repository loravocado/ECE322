import unittest
import sys
# sys.path.append('C:\\Users\\Lora\\Documents\\School\\ECE322\\Lab4\\Lab4_src')

sys.path.append('C:\\Users\\lora_\\Documents\\ECE322\\Lab4\\Lab4_src')

from unittest.mock import Mock
from modules.ModuleD import ModuleD
from data.Entry import Entry

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
    
    def test_updateData(self):
        data = [
            Entry('A', '1'),
            Entry('B', '2'),
            Entry('C', '3'),
            Entry('D', '4'),
        ]
        
        expected = [
            ('A', '1'),
            ('B', '2'),
            ('Z', '22'),
            ('D', '4'),
        ]

        result = self.modD.updateData(data, 2, 'Z', '22', 'fileName.txt')
        self.assertEqual(len(result), 4)
        for i in range(len(result)):
            self.assertEqual(result[i].name, expected[i][0])
            self.assertEqual(result[i].number, expected[i][1])
        self.modF.displayData.assert_called_once_with(result)
        self.modG.updateData.assert_called_once_with('fileName.txt', result)

    def test_deleteData(self):
        data = [
            Entry('A', '1'),
            Entry('B', '2'),
            Entry('C', '3'),
            Entry('D', '4'),
        ]
        
        expected = [
            ('A', '1'),
            ('B', '2'),
            ('D', '4'),
        ]

        result = self.modD.deleteData(data, 2, 'fileName.txt')
        self.assertEqual(len(result), 3)
        for i in range(len(result)):
            self.assertEqual(result[i].name, expected[i][0])
            self.assertEqual(result[i].number, expected[i][1])
        self.modF.displayData.assert_called_once_with(result)
        self.modG.updateData.assert_called_once_with('fileName.txt', result)

    def test_FGetter(self):
        self.modD._f = "Hello"
        self.assertEqual(self.modD.f, "Hello")

    def test_FSetter(self):
        self.modD.f = "Hello"
        self.assertEqual(self.modD._f, "Hello")

    def test_GGetter(self):
        self.modD._g = "Hello"
        self.assertEqual(self.modD.g, "Hello")

    def test_GSetter(self):
        self.modD.g = "Hello"
        self.assertEqual(self.modD._g, "Hello")

if __name__ == '__main__':
    unittest.main()
