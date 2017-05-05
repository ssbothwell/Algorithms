#!/usr/bin/env python

"""
Maximum Weight Independant Set Problem

Given a set of vertices V describing a path in a graph,
find the subgraph of G with maximum total weight and no
adjacent vertices.

For example:
V := [1] - [4] - [5] - [4]
Solution == [4,4] == 8

Given an optimal solution to MWIS, one of the following two
statements is true:
    1. The last element is not part of the optimal set. This
        also means that the last element is not part of any
        subgraph V' of V formed by removing the last element.
    2. The last element is part of the optimal set. This means
        that the second to last element is not part of the
        optimal set or any subgraph V'' of V formed by removing
        the last two elements of V.

If we somehow knew which one of these statements was true for
a given graph. We could then recursively solve the problem.
However, the recursive solution takes exponential time. This is
because we only throw out either 1 or 2 vertices at each recursive
call. So we are branching twice for every 1 or 2 vertices.

However, across all these recursive calls, there are only N
unique sub problems (where N is the size of the origina graph).
These subproblems are all the subgraphs with either 1 or 2 vertex
removed. The exponential runtime of the recursive algorithm is a
result of solving these subproblems over and over again.

If we cache the solutions for each of these subproblems as we
generate them, we can drastically reduce the run time. This is
called 'memoization'. Working from the smallest subgraph (of size 1
and weight G[0]) we can check which of the two statements results
in the max size subgraph and record that in A[i].

Pseudocode:
G = Problem Graph
A = array of max weights of subgraphs
for i in G:
    A[i] = max(A[i-1], A[i-2]+G[i])
return A[-1]
"""

def recursive_mwis(graph):
    # naive recursive version
    if len(graph) == 1:
        return graph[0]
    elif len(graph) < 1:
        return 0
    else:
        s1 = recursive_mwis(graph[:-1])
        s2 = graph[-1] + recursive_mwis(graph[:-2])
        return max(s1,s2)

def mwis(graph):
    V = graph[:]
    for i, el in enumerate(V):
        if i == 0:
            V[i] = V[i]
        elif i == 1:
            V[i] = max(V[i-1], V[i])
        else:
            V[i] = max(V[i-1], V[i-2] + V[i])
    return V

def reconstruct(path):
    """ Returns the indices of the vertices of the MWIS """
    orig = range(1, len(path)+1)
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
    data = [ (int(x[0]), int(x[1])) for x.strip().split(' ') in file]
    return data


if __name__ == '__main__':
    a = [1,4,5,4] #[4,4]
    #a = [280,618,762,908,409,34,59,277,246,779] #[2,4,6,8,10]
    #a = [460,250,730,63,379,638,122,435,705,84] #[1,3,6,9]
    #a = load_path('data_mwis.txt')
    result = reconstruct(mwis(a))
    print(result)
    # This list comprehension is specific to coursera assignment
    #print([ x for x in [1,2,3,4,17,117,517,997] if x in result])
