#!/usr/local/bin/python
import sys

rate_input=float(raw_input("Enter the rate: "))
euros_input=float(raw_input("Enter the number of euros: "))

def cc(rate,euros):
    dollars = rate * euros
    return dollars

print(cc(rate_input,euros_input))
