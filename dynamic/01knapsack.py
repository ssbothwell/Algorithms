#!/usr/bin/env python
import sys
"""
The 0/1 Knapsack Problem

Given a set of items, each with a weight and a value, and a
knapsack with a max weight. What is the subset of items has
a the highest value without exceding the max weight of the
knapsack.

Given a set of all items S and a subset S' which is optimal
subset given the knapsack weight.S' must still be optimal if
an item is removed from it and S.


"""

def knapsack(items, sack):
    """
    items = [(v,w),(v,w)]
    sack = int
    """
    A = [[0] * len(items) for x in range(sack+1)]
    for i in range(0, len(items)):
        for j in range(0, sack+1):
            if items[i][1] > j:
                A[j][i] = A[j][i-1]
            else:
                A[j][i] = max(A[j][i-1], A[j-items[i][1]][i-1] + items[i][0])
    return A

def recursive_knapsack(items, size):
    cache = {}
    def inner(items, size, totalItems, currentItem, cache):
        if currentItem >= totalItems or size <= 0:
            return 0
        key = (totalItems - currentItem -1, size)
        if key in cache:
            return cache[key]
        elif items[currentItem][1] > size:
            maxValue = inner(items, size, totalItems, currentItem+1, cache)
        else:
            maxValue = max(items[currentItem][0] + inner(items, size-items[currentItem][1], totalItems, currentItem+1, cache),
            inner(items, size, totalItems, currentItem+1, cache))

        cache[key] = maxValue
        return maxValue
    return inner(items, size, len(items), 0, cache)

def reconstruct(A, items):
    result = []
    j = len(A)-1
    i = len(A[j])-1
    while j > 1:
        if A[j][i] != A[j][i-1]:
            result.append(i+1)
            j -= items[i][1]
        i -= 1
    return result

def load_items(filename):
    """ Generate graph path from text file """
    file = open(filename, 'r')
    # Map each line of test data to a line in the data list:
    data = [ [int(y) for y in x.rstrip().split(' ')] for x in file]
    return data

def print_result(result, reconstruct_flag=False):
    for i in range(len(result)-1, -1, -1):
        print(i,result[i])
    print('   '+'  '.join([str(x) for x in range(1,len(items)+1)]))
    print("Optimal Value: %s" % result[-1][-1])
    if reconstruct_flag == True:
        print("Items Chosen: %s" % reconstruct(result, items))

if __name__ == '__main__':
    items = [(3,4)
            ,(2,3)
            ,(4,2)
            ,(4,3)
            ]
    result = knapsack(items, 6)
    print_result(result, True)

