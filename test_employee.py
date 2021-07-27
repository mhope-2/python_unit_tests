import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def test_email(self):
        """ Test employee emails """

        emp1 = Employee(first_name='Michael', last_name='Hope', pay=1000000)
        emp2 = Employee(first_name='John', last_name='Hagan', pay=2500)

        self.assertEqual(emp1.email, 'Michael.Hope@email.com')
        self.assertEqual(emp2.email, 'John.Hagan@email.com')

        emp1.first_name = 'Larry'
        emp2.first_name = 'Jay'

        self.assertEqual(emp1.email, 'Larry.Hope@email.com')
        self.assertEqual(emp2.email, 'Jay.Hagan@email.com')


    def test_full_name(self):
        """ Test employee full name """

        emp1 = Employee(first_name='Jay', last_name='Smith', pay=1000000)
        emp2 = Employee(first_name='Say', last_name='Mannor', pay=12500)

        self.assertEqual(emp1.full_name, 'Jay Smith')
        self.assertEqual(emp2.full_name, 'Say Mannor')

    
    def test_apply_raise(self):
        """ Test employee raise """

        emp1 = Employee(first_name='Suzzy', last_name='Jackie', pay=50000.12)
        emp2 = Employee(first_name='Sammy', last_name='Tay', pay=4512.45)

        emp1.apply_raise()
        emp2.apply_raise()

        self.assertEqual(emp1.pay, 52500.126000000004)
        self.assertEqual(emp2.pay, 4738.0725)


if __name__ == '__main__':
    unittest.main()