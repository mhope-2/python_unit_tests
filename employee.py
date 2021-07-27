import requests

class Employee:
    """ A sample employee class. """ 
    raise_amt = 1.05

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

    @property
    def email(self):
        return "{}.{}@email.com".format(self.first_name, self.last_name)

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)
    
    def apply_raise(self):
        self.pay = self.pay * self.raise_amt 
    
    # Mocking
    def monthly_schedule(self, month):
        response = requests.get("http://company.com/{}/{}".format(self.last_name, month))
        if response.ok:
            return response.text
        else:
            return response.status_code