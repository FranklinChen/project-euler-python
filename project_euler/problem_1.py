"""
Problem 1 of Project Euler

http://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or
5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def sum_multiple_3_or_5_below(n):
    """
    Return the sum of multiples of 3 or 5 less than n.

    :param n: natural number upper range
    :return: positive natural number
    """
    return sum(m for m in range(n) if multiple_3_or_5(m))

def multiple_3_or_5(n):
    """
    The trick is to avoid double-counting numbers that are multiples of
    both 3 and 5.  So we cannot count multiples of 3 and multiples of 5
    and add them.

    :param n: natural number upper range
    :return: whether n is a multiple of 3 or 5
    """
    return n % 3 == 0 or n % 5 == 0

def answer():
    return sum_multiple_3_or_5_below(1000)

def print_answer():
    print(answer())
