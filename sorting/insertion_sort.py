#!/usr/bin/env python

def insertion_sort(ar):
    for i in range(0,len(ar)):
        j = i
        while j > 0 and ar[j-1] > ar[j]:
            ar[j], ar[j-1] = ar[j-1], ar[j]
            j = j - 1
    return ar


if __name__ == '__main__':
    arr = [2,4,6,8,3]
    print insertion_sort(arr)