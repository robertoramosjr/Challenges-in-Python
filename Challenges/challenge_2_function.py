"""
1 - create a function that tales another function as parameter e returns the value of function 2.
"""


def func1(func):
    return func


def func2(salutation, name):
    return f'{salutation} {name}, welcome!'


print(func1(func2('Hello', 'Roberto')))


"""
2 - create a function that receives a second function as parameter and returns the 
value of func2 executed. make the first function execute two functions that get a different 
number of arguments
"""


def func1(func, *args, **kwargs):
    return func(*args, **kwargs)


def func2(salutation, name):
    return f'{salutation} {name}, welcome!'


print(func1(func2, 'Hi', 'Roberto'))
