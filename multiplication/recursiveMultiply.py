#!/usr/bin/python
import sys

def multi(a,b):
    if a == 0 or b == 0:
        return 0
    elif a == 1:
        return b
    else:
        return multi(a-1,b) + b

a = 3141592653589793238462643383279502884197169399375105820974944592
b = 2718281828459045235360287471352662497757247093699959574966967627
foo = multi(a,b)
print(foo)
