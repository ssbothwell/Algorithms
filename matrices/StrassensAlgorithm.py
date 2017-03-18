#!/usr/bin/python
# -*- coding: utf-8 -*-
from matrixAddition import addMatrix
from matrixSubtraction import subtractMatrix

def strassen(x,y):
    """
    Calculate the product of two cubic matrices in O(n^2) time.
    Uses 7 recursive calls and clever addition and subtraction
    to achieve this time.

    Recursive Calls:
    P1 ← Strassen(A11, B12 − B22)
    P2 ← Strassen(A11 + A12, B22)
    P3 ← Strassen(A21 + A22, B11)
    P4 ← Strassen(A22, B21 − B11)
    P5 ← Strassen(A11 + A22, B11 + B22)
    P6 ← Strassen(A12 − A22, B21 + B22)
    P7 ← Strassen(A11 − A21, B11 + B12)
    """
    n = len(x)
    # Base Case:
    if n == 1:
        return [[x[0][0] * y[0][0]]]
    else:
        # Subdivide the matrices into quadrants:
        # | a11 a12 |  | b11 b12 |
        # | a21 a22 |  | b21 b22 |
        A11 = [[col for col in row[:len(row)/2]] for row in x[:len(x)/2]]
        A12 = [[col for col in row[len(row)/2:]] for row in x[:len(x)/2]]
        A21 = [[col for col in row[:len(row)/2]] for row in x[len(x)/2:]]
        A22 = [[col for col in row[len(row)/2:]] for row in x[len(x)/2:]]
        B11 = [[col for col in row[:len(row)/2]] for row in y[:len(y)/2]]
        B12 = [[col for col in row[len(row)/2:]] for row in y[:len(y)/2]]
        B21 = [[col for col in row[:len(row)/2]] for row in y[len(y)/2:]]
        B22 = [[col for col in row[len(row)/2:]] for row in y[len(y)/2:]]

        # The 7 recursive calls:
        P1 = strassen(A11, subtractMatrix(B12, B22))
        P2 = strassen(addMatrix(A11, A12), B22)
        P3 = strassen(addMatrix(A21, A22), B11)
        P4 = strassen(A22, subtractMatrix(B21, B11))
        P5 = strassen(addMatrix(A11, A22), addMatrix(B11, B22))
        P6 = strassen(subtractMatrix(A12, A22), addMatrix(B21, B22))
        P7 = strassen(subtractMatrix(A11, A21), addMatrix(B11, B12))

        # Assemble the quadrants of the  product
        C11 = addMatrix(subtractMatrix(addMatrix(P5,P4), P2), P6)
        C12 = addMatrix(P1,P2)
        C21 = addMatrix(P3,P4)
        C22 = subtractMatrix(subtractMatrix(addMatrix(P1,P5), P3),P7)

        # Join the quadrants into the final outpu
        top = join_horiz(C11, C12)
        bottom = join_horiz(C21, C22)
        c = join_vert(top,bottom)
        return c

def join_horiz(a, b):
    return [rowa + rowb for rowa, rowb in zip(a,b)]

def join_vert(a, b):
    return a+b
a = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
    ]
b = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
    ]

answer = [
    [90,100,110,120],
    [202,228,254,280],
    [314,356,398,440],
    [426,484,542,600]
    ]

print strassen(a,b)
