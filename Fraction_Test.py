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
        self.assertEqual(str(Fraction(1, 1)), '1/1')

    def test_add(self):
        pass

if __name__ == '__main__':
    unittest.main()

#ukol task 2 je lepší umí věci zapsat a přečíst bude umět vrátit hodnoty v různých soustávách poskládat třádu a napsat testy. otestovat to jak převádět mezi octa, hexadecimal, binar
# 