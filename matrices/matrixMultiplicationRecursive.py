#!/usr/bin/python

def multiMatrix(x,y):
    n = len(x)
    if n == 1:
        return x[0][0] * y[0][0]
    else:
        a = [[col for col in row[:len(row)/2]] for row in x[:len(x)/2]]
        b = [[col for col in row[len(row)/2:]] for row in x[:len(x)/2]]
        c = [[col for col in row[:len(row)/2]] for row in x[len(x)/2:]]
        d = [[col for col in row[len(row)/2:]] for row in x[len(x)/2:]]
        e = [[col for col in row[:len(row)/2]] for row in y[:len(y)/2]]
        f = [[col for col in row[len(row)/2:]] for row in y[:len(y)/2]]
        g = [[col for col in row[:len(row)/2]] for row in y[len(y)/2:]]
        h = [[col for col in row[len(row)/2:]] for row in y[len(y)/2:]]
        ae = multiMatrix(a,e)
        bg = multiMatrix(b,g)
        af = multiMatrix(a,f)
        bh = multiMatrix(b,h)
        ce = multiMatrix(c,e)
        dg = multiMatrix(d,g)
        cf = multiMatrix(c,f)
        dh = multiMatrix(d,h)

        c = [[ae+bg,af+bh],[ce+dg,cf+dh]]

        return c


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

print multiMatrix(a,b)
