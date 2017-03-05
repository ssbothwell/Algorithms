#!/usr/bin/env python
import random
import time

def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print '%r (%r, %r) %2.2f sec' % \
              (method.__name__, args, kw, te-ts)
        return result

    return timed

def partition(array,start,end):
    """ median of three """
    """ not my code """
    global comparisons
    comparisons += (end-start)-1
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

def findMedianOfThree(a, l, r):
    arr = a[l:r]
    threes = [arr[0], arr[-1]]
    if len(arr) % 2 != 0:
        threes.append(arr[len(arr)//2])
    else:
        threes.append(arr[len(arr)//2 - 1])

    return a.index(sorted(threes)[1])
#def partition(a, l, r):
#    """ first element pivot """
#    global comparisons
#    p = a[l]
#    i = l + 1
#    comparisons += (r-l)-1
#    for j in range(l+1, r):
#        if a[j] < p:
#            a[j], a[i] = a[i], a[j]
#            i += 1
#    a[l], a[i-1] = a[i-1], a[l]
#
#    return i-1

#def partition(a, l, r):
#    """ Swap final element with First Element """ 
#    global comparisons
#    a[l], a[r] = a[r], a[l]
#    p = a[l]
#    i = l + 1
#    comparisons += (r-l)-1
#    for j in range(l+1, r):
#        if a[j] < p:
#            a[j], a[i] = a[i], a[j]
#            i += 1
#        #comparisons += 1
#    a[l], a[i-1] = a[i-1], a[l]
#
#    return i-1
#def partition(a, l, r):
#    """ final element pivot """
#    global comparisons
#    p = a[r-1]
#    i = l - 1
#    comparisons += (r-l)-1
#    for j in range(l, r-1):
#        if a[j] <= p:
#            i += 1
#            a[j], a[i] = a[i], a[j]
#        #comparisons += 1
#    a[r-1], a[i+1] = a[i+1], a[r-1]
#
#    return i+1
def quickSort(arr, l=0, r=None):
    if r == None:
        r = len(arr)
    if l >= r:
        return
    p = partition(arr, l, r)
    quickSort(arr, l, p)
    quickSort(arr, p+1, r)


comparisons = 0
@timeit
def outer():
    global comparisons
    file = open('quickSortData.txt', 'r')
    data = [ int(line.rstrip()) for line in file ] 
    #data = [8,3,4,6,2,5,7,1]
    quickSort(data)
    print data
    print comparisons

outer()


