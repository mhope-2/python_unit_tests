import unittest
from employee import Employee
import requests

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ Runs once at the very beginning before the test"""
        print("setUpClass")


    @classmethod
    def tearDownClass(cls):
        """ Runs once at the very end after the test"""
        print("tearDownClass")

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

        self.emp1.first_name = 'Karen'
        self.emp2.first_name = 'Sue'

        self.assertEqual(self.emp1.full_name, 'Karen Hope')
        self.assertEqual(self.emp2.full_name, 'Sue Hagan')

    
    def test_apply_raise(self):
        """ Test employee raise """


        self.emp1.apply_raise()
        self.emp2.apply_raise()

        self.assertEqual(self.emp1.pay, 52500)
        self.assertEqual(self.emp2.pay, 63000)

    
    # Mocking
    def monthly_schedule(self, month):
        response = requests.get("http://company.com/{}/{}".format(self.last_name, month))
        if response.ok:
            return response.text
        else:
            return response.status_code


if __name__ == '__main__':
    unittest.main()