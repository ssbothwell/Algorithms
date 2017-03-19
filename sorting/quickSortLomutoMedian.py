#!/usr/bin/env python
import random
import time
#
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

#    return timed

def partition(array,start,end):
    """ median of three """
    """ not my code """
    median = (end -1 - start) / 2
    median = median + start
    left = start + 1
    if (array[median] - array[end-1])*(array[start]-array[median]) >= 0:
        array[start], array[median] = array[median], array[start]
    elif (array[end - 1] - array[median]) * (array[start] - array[end - 1])>= 0:
        array[start], array[end-1] = array[end-1], array[start]
    pivot = array[start]
    for right in range(start,end):
        if pivot > array[right]:
            array[left], array[right] = array[right], array[left]
            left = left + 1
    array[start], array[left-1] = array[left-1], array[start]
    return left-1

#def findMedianOfThree(a, l, r):
#    arr = a[l:r]
#    threes = [arr[0], arr[-1]]
#    if len(arr) % 2 != 0:
#        threes.append(arr[len(arr)//2])
#    else:
#        threes.append(arr[len(arr)//2 - 1])
#
#    return a.index(sorted(threes)[1])

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

