""" These are functions. """
import random
def myfunc():
    """ Return a thing. """
    return random.randint(0, 100)
def multiply(value_one, value_two):
    """ Return a thing. """
    return value_one * value_two

print(multiply(myfunc(), myfunc()))
