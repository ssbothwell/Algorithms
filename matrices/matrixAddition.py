#!/usr/bin/python

def addMatrix(x, y):
    """ Params: two matrices as nested lists """
    """ Returns: their sum if they are the same size """
    """ Otherwise or -1 """

    # Check inputs
    if isinstance(x, (int, long)):
        return x+y
    if len(x) != len(y):
        return -1
    for row in range(0,len(x)):
        if len(x[row]) != len(y[row]):
            return -1
    z = []
    for row in range(0,len(x)):
        z.append([])
        for col in range(0, len(x[row])):
            z[row].append(x[row][col]+y[row][col])

    return z


#a = [[0,1,2],[9,8,7]]
#b = [[6,5,4],[3,4,5]]
#
#print addMatrix(a,b)
