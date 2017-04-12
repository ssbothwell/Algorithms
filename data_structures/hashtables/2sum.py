#!/usr/bin/env python
from bisect import bisect_left,bisect_right

def load_data(filename):
    """ Generate sorted unique list from text file """
    file = open(filename, 'r')
    data = set()
    for line in file:
        data.add(int(line))
    return sorted(data)


def sum_calc(data_arr):
    target_tally = set()
    for val in data_arr:
        low = bisect_left(data_arr, -10000 - val)
        high = bisect_right(data_arr, 10000 - val)
        for pair in data_arr[low:high]:
            if pair != val:
                target_tally.add(val + pair)
    return len(target_tally)

if __name__ == '__main__':
    #data = sorted([-3,-1,1,2,9,11,7,6,2])
    #data = [0,1,2,3,4,5,6]
    data = load_data('data_2sum.txt')
    print sum_calc(data)
    #print len(filter(lambda x: x == True, [ sum_calc(data, x) for x in range(3,5)]))
