#!/usr/bin/python
import sys

def rMulti(a,b):
    if a == 0 or b == 0:
        return 0
    elif a > 0:
        return rMulti(a-1,b) + b
    else:
        return rMulti(a+1, b) - b

