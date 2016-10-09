#!/usr/local/bin/python
import sys

#input_temp=int(raw_input("Enter the temperature in Celsius: "))
#cel_temp=32
temperatures=[10,-20,-289,100]

def c2f(cel_temp):
    if cel_temp < -273.15:
        return "The lowest possible temperature that physical matter can reach is -273.15C"
    else:
        fah_temp=(cel_temp*1.8)+32
        return fah_temp


for temp in temperatures:
    print(c2f(temp))
