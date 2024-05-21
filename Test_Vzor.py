import unittest
from Calculator import Calculator




class TestMathFunctions(unittest.TestCase):
    def setUp(self):
        self.c = Calculator()

    def test_addition(self):
        self.assertEqual(self.c.add(2, 3), 5)
        self.assertEqual(self.c.add(9, 9), 18)
        self.assertEqual(self.c.add(2, -3), -1)
        self.assertEqual(self.c.add(2, -1), 1)
        self.assertEqual(self.c.add(-2, 3), 1)
        self.assertEqual(self.c.add(-4, 3), -1)
        self.assertEqual(self.c.add(-2, -3), -5)
        self.assertEqual(self.c.add(-9, -9), -18)
        self.assertEqual(self.c.add(0, 0), 0)
        self.assertEqual(self.c.add(1, 0), 1)
        self.assertEqual(self.c.add(0, 1), 1)
        self.assertEqual(self.c.add(0, -1), -1)
        self.assertEqual(self.c.add(-1, 0), -1)
        self.assertEqual(self.c.add(999999999, 1), 1000000000)
        self.assertEqual(self.c.add(1, 999999999), 1000000000)

    def test_addition_fraction(self):
        self.assertAlmostEqual(self.c.add(2.2, 3.2), 5.4, places=7)
        self.assertAlmostEqual(self.c.add(9.2, 9.2), 18.4, places=7)
        self.assertAlmostEqual(self.c.add(2.2, -3.2), -1, places=7)
        self.assertTrue(self.c.add(2.2, -3.1) - (-0.9) < 0.000001)
        self.assertAlmostEqual(self.c.add(2.2, -3.1), -0.9, places=7)
        self.assertAlmostEqual(self.c.add(2.2, -1.2), 1, places=7)


    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            self.c.divide(3, 0)



if __name__ == '__main__':
    unittest.main()