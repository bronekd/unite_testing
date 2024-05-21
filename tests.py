# text vzor od učitele
import unittest

def add(a, b):
    return a + b
class TestMathFunctions(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 2), 0)

    def test_addition2(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()

