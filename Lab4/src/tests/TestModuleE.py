import unittest
from unittest.mock import patch
import sys
# sys.path.append('C:\\Users\\Lora\\Documents\\School\\ECE322\\Lab4\\Lab4_src')

sys.path.append('C:\\Users\\lora_\\Documents\\ECE322\\Lab4\\Lab4_src')

from modules.ModuleE import ModuleE

from unittest.mock import Mock
from unittest.mock import patch

class TestModuleE(unittest.TestCase):  
    def setUp(self):
        self.modE = ModuleE()

    def test_exit(self):
        with self.assertRaises(SystemExit) as cm:
            self.modE.exitProgram()
            self.assertEqual(cm.exception.code, 1)

if __name__ == '__main__':
    unittest.main()
