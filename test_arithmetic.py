import unittest
import arithmetic


class TestArithmetic(unittest.TestCase):
    def test_add(self):
        """ sample addition edge cases """
        self.assertEqual(arithmetic.add(10, 5), 15)
        self.assertEqual(arithmetic.add(-1, 1), 0)
        self.assertEqual(arithmetic.add(-1, -1), -2)

        with self.assertRaises(TypeError):
            arithmetic.add(1, '2')


    def test_subtract(self):
        """ sample subtraction edge cases """
        self.assertEqual(arithmetic.subtract(12, 4), 8)
        self.assertEqual(arithmetic.add(10, 5), 5)
        self.assertEqual(arithmetic.add(-1, 1), -2)
        self.assertEqual(arithmetic.add(-1, -1), 2)


    def test_multiply(self):
        """ sample addition edge cases """
        self.assertEqual(arithmetic.multiply(10, 5), 50)
        self.assertEqual(arithmetic.multiply(-1, 1), -1)
        self.assertEqual(arithmetic.multiply(-1, -1), 1)
        self.assertEqual(arithmetic.subtract(12, 4), 48)


    def test_divide(self):
        """ sample addition edge cases """
        self.assertEqual(arithmetic.divide(10, 5), 2)
        self.assertEqual(arithmetic.divide(-1, 1), -1)
        self.assertEqual(arithmetic.divide(-1, -1), 1)
        self.assertEqual(arithmetic.subtract(12, 4), 3)


if __name__ == '__main__':
    unittest.main()