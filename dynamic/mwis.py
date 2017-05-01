#!/usr/bin/env python

"""
Maximum Weight Independant Set Problem

Given a set of vertices V describing a path in a graph,
find the subgraph of G with maximum total weight and no
adjacent vertices.

For example:
V := [1] - [4] - [5] - [4]
Solution == [4,4] == 8

For any optimal solutionto MWIS, one of the following two
statements is true:
    1. The last element is not part of the optimal set. This
        also means that the last element is not part of any
        subgraph V' of V formed by removing the last element.
    2. The last element is part of the optimal set. This means
        that the second to last element is not part of the
        optimal set or any subgraph V'' of V formed by removing
        the last two elements of V.

"""

def mwis(graph):
    V = graph[:]
    for i, el in enumerate(V):
        if i == 0:
            V[i] = V[i]
        elif i == 1:
            if V[i-1] > el:
                V[i] = V[i-1]
            else:
                    V[i] = V[i]
        else:
            if V[i-1] > V[i-2] + V[i]:
                V[i] = V[i-1]
            else:
                V[i] = V[i-2] + V[i]
    return V

def reconstruct(path, orig):
    result = []
    i = len(path)-1
    while i >= 1:
        if path[i] == path[i-1]:
            i -= 1
        else:
            result.append(orig[i])
            i -= 2
    if i == 0:
        result.append(orig[i])
    return result

def load_path(filename):
    """ Generate graph path from text file """
    file = open(filename, 'r')
    # Map each line of test data to a line in the data list:
    data = [ int(x.strip()) for x in file]
    return data


if __name__ == '__main__':
    #a = [1,4,5,4] #[4,4]
    #a = [280,618,762,908,409,34,59,277,246,779] #[2,4,6,8,10]
    #a = [460,250,730,63,379,638,122,435,705,84] #[1,3,6,9]
    a = load_path('data_mwis.txt')
    j = range(1, len(a)+1)
    result = reconstruct(mwis(a), j)
    print([ x for x in [1,2,3,4,17,117,517,997] if x in result])
