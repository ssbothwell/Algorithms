#!/usr/bin/env python

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
    A = [[ 0 for x in range(0, len(items))] for y in range(sack+1)]
    for i in range(0, len(items)):
        for j in range(0, sack+1):
            if items[i][1] > j:
                A[j][i] = A[j][i-1]
            else:
                A[j][i] = max(A[j][i-1], A[j-items[i][1]][i-1] + items[i][0])
    return A

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


if __name__ == '__main__':
    items = [(3,4)
            ,(2,3)
            ,(4,2)
            ,(4,3)
            ]
    items = load_items('data_knapsack1.txt')
    result = knapsack(items, len(items))
    for i in range(len(result)-1, -1, -1):
        print(i,result[i])
    #print('   '+'  '.join([str(x) for x in range(1,len(items)+1)]))
    print("Optimal Value: %s" % result[-1][-1])
    #print("Items Chosen: %s" % reconstruct(result, items))
