#!/usr/bin/env python

import sys

# Ask user to input a number
number = input("Enter a number: ")

if number % 2 == 0:
    print(str(number) + " is an even number.")
elif number % 2 == 1:
    print(str(number) + " is an odd number.")
