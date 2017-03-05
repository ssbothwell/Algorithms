#!/usr/bin/python

def karat(x,y):
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

a = 3141592653589793238462643383279502884197169399375105820974944592
b = 2718281828459045235360287471352662497757247093699959574966967627
foo = karat(a,b)

print(foo)
