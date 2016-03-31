#!/usr/bin/env python

# http://usingpython.com/python-text/

import sys
import os

os.system('clear')

i = 0

for i in range(1, int(sys.argv[1])):
    print ("*" * i + "\n")
