import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp1 = Employee(first_name='Michael', last_name='Hope', pay=50000)
        self.emp2 = Employee(first_name='John', last_name='Hagan', pay=60000)

    def tearDown(self):
        pass

    def test_email(self):
        """ Test employee emails """

        self.assertEqual(self.emp1.email, 'Michael.Hope@email.com')
        self.assertEqual(self.emp2.email, 'John.Hagan@email.com')

        self.emp1.first_name = 'Larry'
        self.emp2.first_name = 'Jay'

        self.assertEqual(self.emp1.email, 'Larry.Hope@email.com')
        self.assertEqual(self.emp2.email, 'Jay.Hagan@email.com')


    def test_full_name(self):
        """ Test employee full name """

        self.assertEqual(self.emp1.full_name, 'Jay Smith')
        self.assertEqual(self.emp2.full_name, 'Say Mannor')

    
    def test_apply_raise(self):
        """ Test employee raise """


        self.emp1.apply_raise()
        self.emp2.apply_raise()

        self.assertEqual(self.emp1.pay, 52500)
        self.assertEqual(self.emp2.pay, 63000)


if __name__ == '__main__':
    unittest.main()