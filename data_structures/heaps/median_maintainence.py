#!/usr/bin/python
from binHeap import *


def createList(filename):
    """ Generate edge list from text file """
    file = open(filename, 'r')
    return  map(lambda x: int(x.rstrip()), file)

def mean(a,b):
    return (a+b)/2

def median_maintainence(arr):
    h_low = max_heap()
    h_high = min_heap()
    m = 0
    m_history = 0
    for i in arr:
        if len(h_low.heap_list) == len(h_high.heap_list):
        ## If both heaps have the same number of elements 
            if i < m or len(h_low.heap_list) == 1:
                # `i` is less then the mean 
                h_low.insert(i)
                m = sum(h_low.heap_list[:2])
            else:
                # `i` is more then the mean 
                h_high.insert(i)
                m = sum(h_high.heap_list[:2])

        elif len(h_low.heap_list) > len(h_high.heap_list):
        ## If h_low (max heap) has more elements
            if i < m:
                # `i` is less then the mean 
                h_high.insert(h_low.del_min())
                h_low.insert(i)
            else:
                # `i` is more then the mean 
                h_high.insert(i)
            # recalculate mean
            m = mean(h_low.heap_list[1],h_high.heap_list[1])

        else:
        ## If h_high (min heap) has more elements
            if i < m:
                # `i` is less then the mean 
                h_low.insert(i)
            else:
                # `i` is more then the mean
                h_low.insert(h_high.del_min())
                h_high.insert(i)

            # recalculate mean
            m = mean(h_low.heap_list[1],h_high.heap_list[1])

        ## Update median sum
        # [x1..xk] is total processed array between the two 
        # heaps at this point. If [x1..xk] is odd then median
        # is the ((k+1)/2)th element, if [x1..xk] is even then
        # the median is (k/2)th element. 
        #
        # This can easily be checked by comparing the heap 
        # lengths:
        #   -same Size: even
        #   -Different Sizes: odd
        # When they are even, the median is always on the top
        # h_low. When They are odd, the median is on top of the
        # larger heap.

        if len(h_low.heap_list) < len(h_high.heap_list):
            # if [x1..xk] is odd, median is in h_high: 
            m_history += sum(h_high.heap_list[:2])
        else:
            # if [x1..xk] is even, median is in h_low 
            m_history += sum(h_low.heap_list[:2])

    out = m_history % 10000
    return out

if __name__ == '__main__':
    test = [1, 666, 10, 667, 100, 2, 3]
    test2 = [6331, 2793, 1640, 9290, 225, 625, 6195, 2303, 5685, 1354]
    l = createList("median.txt")
    print median_maintainence(l)
