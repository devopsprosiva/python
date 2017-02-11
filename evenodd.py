#!/usr/bin/env python

import sys

# Ask user to input a number
number = input("Enter a number: ")


# The % (modulo) operator yields the remainder from the division of the first argument by the second.
# The numeric arguments are first converted to a common type.
# A zero right argument raises the ZeroDivisionError exception.
# The arguments may be floating point numbers, e.g., 3.14%0.7 equals 0.34 (since 3.14 equals 4*0.7 + 0.34.)
# The modulo operator always yields a result with the same sign as its second operand (or zero); the absolute value of the result is strictly smaller than the absolute value of the second operand [2].
# Taken from http://docs.python.org/reference/expressions.html

if number % 2 == 0:
    print(str(number) + " is an even number.")
elif number % 2 == 1:
    print(str(number) + " is an odd number.")
