
def add(num1, num2):
    """ add function """
    return num1 + num2


def subtract(num1, num2):
    """ subtract function """
    return num1 - num2


def multiply(num1, num2):
    """ multiply function """
    return num1 * num2


def divide(num1, num2):
    """ divide function """

    if num2 == 0:
        raise ValueError('Can not divide by zero!')
    return num1 / num2


    
    