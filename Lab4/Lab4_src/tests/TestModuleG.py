import unittest
from unittest.mock import patch, mock_open, call
import sys
# sys.path.append('C:\\Users\\Lora\\Documents\\School\\ECE322\\Lab4\\Lab4_src')

sys.path.append('C:\\Users\\lora_\\Documents\\ECE322\\Lab4\\Lab4_src')

from modules.ModuleG import ModuleG
from data.Entry import Entry
from unittest.mock import patch

class TestModuleE(unittest.TestCase):  
    def setUp(self):
        self.modG = ModuleG()

    @patch('builtins.open', new_callable=mock_open)
    def test_updateData(self, fileMock):
        data = [
            Entry('A', '1'),
            Entry('B', '2'),
            Entry('C', '3'),
            Entry('D', '4'),
        ]
        calls = [
            call('A,1\n'),
            call('B,2\n'),
            call('C,3\n'),
            call('D,4\n'),
        ]
        
        self.modG.updateData('fakefile', data)

        # Assert file is opened properly
        fileMock.assert_called_once_with('fakefile', 'w')

        # Assert data is properly logged in file and closed
        file = fileMock()

        self.assertEqual(file.write.call_count, 4)
        file.write.assert_has_calls(calls)
        file.__exit__.assert_called()

if __name__ == '__main__':
    unittest.main()
