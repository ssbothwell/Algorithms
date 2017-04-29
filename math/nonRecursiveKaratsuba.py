#!/usr/bin/python

def karat(x,y):
    if x < 10 or y < 10:
        return x*y

    a = int(str(x)[:(len(str(x))/2)])
    b = int(str(x)[(len(str(x))/2):])
    c = int(str(y)[:(len(str(y))/2)])
    d = int(str(y)[(len(str(y))/2):])

    step1 = a * c
    step2 = b * d
    step3 = (a+b)*(c+d)
    step4 = step3 - step2 - step1

    answer = (10**(len(str(x))) * step1) + step2 + (10**((len(str(x)))/2)*step4)

    return answer

