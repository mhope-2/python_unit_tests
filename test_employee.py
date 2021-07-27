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
        self.assertEqual(emp1.email, 'Jay.Hagan@email.com')


    def test_full_name(self):
        """ Test employee full name """

        emp1 = Employee(first_name='Jay', last_name='Smith', pay=1000000)
        emp2 = Employee(first_name='Say', last_name='Mannor', pay=12500)

        self.assertEqual(emp1.full_name, 'Jay Smith')
        self.assertEqual(emp2.full_name, 'Say Mannor')









