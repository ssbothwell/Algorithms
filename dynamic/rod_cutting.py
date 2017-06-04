#!/usr/bin/env python
import sys
"""
The Rod Cutting Problem

Given a  rod of length n, and a table of prices Pi for i = 1,2..n,
determine the maximum revenue obtainable by cutting up the rod and
selling the pieces.

Example:

    price table:
        length i :  1 2 3 4 5  6  7  8  9  10
        price Pi :  1 5 8 9 10 17 17 20 24 30

    solutions for various lengths of rod:
        r1 = 1 from solution 1 = 1 (no cuts)
        r2 = 5 from solution 2 = 2 (no cuts)
        r3 = 8 from solution 3 = 3 (no cuts)
        r4 = 10 from solution 4 = 2+2
        r5 = 13 from solution 5 = 2+3
        r6 = 17 from solution 6 = 6 (no cuts)
        r7 = 18 from solution 7 = 1 + 6 or 7 = 2 + 2 + 3
        r8 = 22 from solution 8 = 2 + 6
        r9 = 25 from solution 9 = 3 + 6
        r10 = 30 from solution 10 = 10 (no cuts)

"""

def cut_rod(p,n):
    if n <= 0:
        return 0
    q = -1
    for i in range(0,n):
        q = max(q, p[i]+ cut_rod(p, n-i-1))
    return q

if __name__ == '__main__':

    price = [ 1,5,8,9,10,17,17,20,24]#,30 ]
    length = len(price)
    print(cut_rod(price, length))
