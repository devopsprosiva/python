#!/usr/local/bin/python
import sys

input_temp=int(raw_input("Enter the temperature in Celsius: "))
#cel_temp=32

def c2f(cel_temp=input_temp):
    if cel_temp < -273.15:
        return "The lowest possible temperature that physical matter can reach is -273.15C"
    else:
        fah_temp=(cel_temp*1.8)+32
        return fah_temp

print(c2f(input_temp))
