#!/usr/bin/env python

#################################################################################################################
# Take a list and write a program that prints out all the elements of the list that are less than 5
#
# Extras:
#   Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
#   Write this in one line of Python.
#   Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
#################################################################################################################

import sys

#l = [1,3,5,7,9,10,12,15,24,55]

# Prompt user to input a list of numbers
user_input = raw_input("Enter a list of numbers separated by a space: ")

# Split the list of numbers using space and assign them to a new list
# Remember that the elements in this list are strings
user_list = user_input.split()

# Convert the string elements in the list to integers
input_list = [int(x) for x in user_list]

# Create an empty output list
output_list = []
#
# # Loop through the list and store elements less than 5 in the output list
# for i in input_list:
#     if i < 5:
#         output_list.append(i)
#
# # Print the final output list
# print output_list

# Same logic as above in a single line
endlist = [i for i in input_list if i<5]
print sorted(endlist)
