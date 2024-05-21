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

    def test_addition_fraction(self):
        self.assertEqual(Calculator.add(2, 0.5), 2.5)
        self.assertEqual(Calculator.add(2.2, 2.5), 4.7)
        self.assertEqual(Calculator.add(0.2, 0.2), 0.4)
        self.assertAlmostEqual(Calculator.add(2.2, -3.1), -0.89999999999999, places=7) #použití pro desetiné číslo

    #def test_division_by_zero(self):
    #    # test chyb a vyjímek
    #    with self.assertRaises(ValueError):
    #        self.Calculator.divide(3,0)
    #zjistiti proč to nefunguje!!!!




if __name__ == '__main__':
    unittest.main()