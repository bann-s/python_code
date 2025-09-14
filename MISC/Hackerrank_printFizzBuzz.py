#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    x = 1
    while x <= n:
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz")
        elif x % 3 == 0:
            print("Fizz")
        elif (x % 5 == 0):
            print("Buzz")
        else:
            print(x)
        x += 1
            # Write your code here

if __name__ == '__main__':