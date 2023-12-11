import unittest
from calc import plus, minus, multiply, divide

class TestCalculator(unittest.TestCase):
    def test_plus(self):
        self.assertEqual(plus(2, 3), 5)

    def test_minus(self):
        self.assertEqual(minus(5, 2), 3)

    def test_multiply(self):
        self.assertEqual(multiply(2, 4), 8)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        with self.assertRaises(ValueError):
            divide(4, 0)

if __name__ == '__main__':
    unittest.main()
