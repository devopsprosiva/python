#!/usr/local/bin/python

#################################################################################################################
# Create a program that asks the user to enter their name and their age.                                        #
# Print out a message addressed to them that tells them the year that they will turn 100 years old.             #
#################################################################################################################

import sys

# input function in Python 2.7, evaluates whatever your enter, as a Python expression.
# If you simply want to read strings, then use raw_input function in Python 2.7, which will not evaluate the read strings.
# If you are using Python 3.x, raw_input has been renamed to input

# Using raw_input for string
name = raw_input("Enter your name: ")

# Using input for integers as it will automatically interpret as number
age = input("Enter your age: ")

# Calculate the number of years remaining to reach 100 years
years_to_hundred = 100 - age

# To assign a value to a variable, use '='
# To compare values of two variables/operands, use '=='
if years_to_hundred == 0:
    print(name + ", you already reached 100.. Yay!!!")
else:
    # Since a string and an integer cannot be concatenated in the same print statement,
    # converting years_to_hundred to string using the str function
    print(name + ", you will be hundred in " + str(years_to_hundred) + " years")
