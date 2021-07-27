import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def test_email(self):
        emp1 = Employee(first_name='Michael', last_name='Hope', pay=1000000)
        emp2 = Employee(first_name='John', last_name='Hagan', pay=2500)

        self.assertEqual(emp1.email, 'Michael.Hope@email.com')
        self.assertEqual(emp2.email, 'John.Hagan@email.com')

        emp1.first_name = 'Larry'
        emp1.last_name = 'Jay'

        self.assertEqual(emp1.email, 'Larry.Jay@email.com')










