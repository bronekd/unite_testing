import unittest
from Fraction_v2 import Fraction

class TestFraction(unittest.TestCase):

    def test_simplify(self):
        f1 = Fraction(20,20)
        f1.simplify()
        f2 = Fraction(6, 6)
        f2.simplify()
        self.assertEqual(f1,Fraction(1,1))
        self.assertEqual(f2, Fraction(1, 1))

    def test_str(self):
        pass

    def test_add(self):
        pass

if __name__ == '__main__':
    unittest.main()