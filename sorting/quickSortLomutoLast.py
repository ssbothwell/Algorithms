#!/usr/bin/env python
import random
#import time

#def timeit(method):
#
#    def timed(*args, **kw):
#        ts = time.time()
#        result = method(*args, **kw)
#        te = time.time()
#
#        print '%r (%r, %r) %2.2f sec' % \
#              (method.__name__, args, kw, te-ts)
#        return result
#
#    return timed

def partition(a, l, r):
    """ final element pivot """
    p = a[r-1]
    i = l - 1
    for j in range(l, r-1):
        if a[j] <= p:
            i += 1
            a[j], a[i] = a[i], a[j]
    a[r-1], a[i+1] = a[i+1], a[r-1]

    return i+1

def quickSort(arr, l=0, r=None):
    if r == None:
        r = len(arr)
    if l >= r:
        return
    p = partition(arr, l, r)
    quickSort(arr, l, p)
    quickSort(arr, p+1, r)


#file = open('quickSortData.txt', 'r')
#data = [ int(line.rstrip()) for line in file ] 
#data = [8,3,4,6,2,5,7,1]
#@timeit
def quickSortOuter(data):
    quickSort(data)
    return data

