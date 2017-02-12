#!/usr/bin/env python

#################################################################################################################
# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to
# the user.
#
# Extras:
#   If the number is a multiple of 4, print out a different message.
#   Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
#   If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
#################################################################################################################

import sys

# Ask user to input a number
number = input("Enter a number: ")

# Ask user to input a number to divide by
check = input("Enter a number to divide by: ")

# The % (modulo) operator yields the remainder from the division of the first argument by the second.
# The numeric arguments are first converted to a common type.
# A zero right argument raises the ZeroDivisionError exception.
# The arguments may be floating point numbers, e.g., 3.14%0.7 equals 0.34 (since 3.14 equals 4*0.7 + 0.34.)
# The modulo operator always yields a result with the same sign as its second operand (or zero); the absolute value of the result is strictly smaller than the absolute value of the second operand [2].
# Taken from http://stackoverflow.com/questions/4432208/how-does-work-in-python , http://docs.python.org/reference/expressions.html


if number % 4 == 0:
    print(str(number) + " is a multiple of 4 and an even number")
elif number % 2 == 0:
    print(str(number) + " is an even number")
elif number % 2 == 1:
    print(str(number) + " is an odd number")


if number % check == 0:
    print(str(number) + " divides evenly by " + str(check))
else:
    print(str(number) + " does not divide evenly by " + str(check))
