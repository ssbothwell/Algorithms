#!/usr/bin/env python
from random import randint

def rSelect(arr, k, left=0, right=None):
    if right == None:
        right = len(arr)
    if left == right:
        return arr[left]
    if left < right:
        j = partition(a,left, right)

        if k == j:
            return arr[k]
        if k < j:
            return rSelect(arr, k, left, j)
        if k > j:
            return rSelect(arr, k, j+1, right)

def partition(a, l, r):
    """ randomized pivot """

    p = randint(l,r-1)
    a[l], a[p] = a[p], a[l]
    i = l + 1
    for j in range(l+1, r):
        if a[j] < a[l]:
            a[j], a[i] = a[i], a[j]
            i += 1
    a[l], a[i-1] = a[i-1], a[l]

    return i-1


a = [ 7,5,4,3,2,1 ]
print rSelect(a, 3)
