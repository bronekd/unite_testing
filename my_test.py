# můj test sčítání:

import unittest
from Calculator import *

class TestMathFunctions(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(Calculator.add(2, 3), 5)
        self.assertEqual(Calculator.add(-1, 1), 0)
        self.assertEqual(Calculator.add(-1, -1), -2)
        self.assertEqual(Calculator.add(-1, 0), -1)
        self.assertEqual(Calculator.add(0, 0), 0)
        self.assertEqual(Calculator.add(0, 5), 5)
        self.assertEqual(Calculator.add(-10, 5), -5)


if __name__ == '__main__':
    unittest.main()