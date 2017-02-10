#!/usr/local/bin/python

import sys

# input function in Python 2.7, evaluates whatever your enter, as a Python expression.
# If you simply want to read strings, then use raw_input function in Python 2.7, which will not evaluate the read strings.
# If you are using Python 3.x, raw_input has been renamed to input

name = raw_input("Enter your name: ")
age = raw_input("Enter your age: ")

print("Your name is " + name)
print("Your age is " + age)
