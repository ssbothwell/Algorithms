#!/usr/bin/python

def matrixMulti(a, b):
    # a = n x m
    # b = m x p
    n = len(a)
    m = len(a[0])
    p = len(b)

    i = 0
    j = 0
    k = 0
    c = [[ 0 for column in b ] for row in a ]

    # Loop through Rows of A
    for i,row in enumerate(a):
        # Loop through columns of B
        for j,column in enumerate(b[0]):
            # Loop through rows of B
            for k, rowB in enumerate(b):
                c[i][j] += a[i][k] * b[k][j]

    return c
x = ((1,2),(3,4))
y = ((1,2),(3,4))

print matrixMulti(x,y)
