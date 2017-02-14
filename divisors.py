#!/usr/bin/env python

#################################################################################################################
# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# http://www.practicepython.org/exercise/2014/02/26/04-divisors.html
#################################################################################################################


import sys

# Ask user for input number
user_input = int(raw_input("Enter a number: "))

# Create an empty output list for divisors
divisors_output_list = []

# Loop through range from 1 to user_input and find numbers that evenly divide the user_input
# Adding 1 to the user_input in the range to include the number itself as the divisor i.e., a number will divide itself evenly
divisors_output_list = [i for i in range(1, user_input+1) if user_input % i == 0]

print divisors_output_list
