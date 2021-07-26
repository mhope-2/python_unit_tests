import unittest
import arithmetic


class TestArithmetic(unittest.TestCase):
    def test_add(self):
        self.assertEqual(arithmetic.add(10, 5), 15)
        self.assertEqual(arithmetic.add(-1, 1), 0)
        self.assertEqual(arithmetic.add(-1, -1), -2)

        with self.assertRaises(TypeError):
            arithmetic.add(1, '2')

