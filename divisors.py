#!/usr/bin/env python

#################################################################################################################
# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
#################################################################################################################


import sys

# Ask user for input number
user_input = int(raw_input("Enter a number: "))

# Create an empty output list for divisors
divisors_output_list = []

# Loop through range from 1 to user_input and find numbers that evenly divide the user_input
divisors_output_list = [i for i in range(1, user_input) if user_input % i == 0]

print divisors_output_list
