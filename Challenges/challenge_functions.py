"""
1 - Create a function that prints a salutation with the par salutation and name.
"""


def salutation(sal, name):
    print(f'{sal} {name}!!!')

"""
2 - Create a function that takes 3 numbers as parameters and prints the sum between then.
"""


def sum_three_numbers(num1, num2, num3):
    print(num1 + num2 + num3)

"""
3 - Create a function that takes 2 numbers. The first is a value and the second a percentile (ex. 10%). 
Return the value of the first number summed by the percentual increase of the same.
"""


def percentile_sum(num1, percentile):
    num1 = num1 + ((percentile/100)*num1)
    return num1


"""
4 - Fizz Buzz - If the function parameter is divisible by 3, returns fiiz, if it's divisible by 5, returns buzz. 
If it's divisible by 5 and 3 returns fizz-buzz. If it's not divisible by 3 or 5 or both, returns the sent number.
"""


def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'Fizz-Buzz'
    if num % 5 == 0:
        return 'Buzz'
    if num % 3 == 0:
        return 'Fizz'
    return f'{num}'

