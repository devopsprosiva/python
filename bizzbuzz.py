#!/usr/bin/env python

# Python exercise based on https://github.com/jasonkeene/mosi-python-workshop/blob/master/0045_exercise_bizzbuzz.ipynb

for i in range(1,200):
    if i%3 == 0 and i%5 == 0:
        print "BizzBuzz"
    elif i%3 == 0:
        print "Bizz"
    elif i%5 ==0 :
        print "Buzz"
    else:
        print i
