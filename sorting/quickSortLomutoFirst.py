#!/usr/bin/env python
from typing import List, TypeVar
Ord = TypeVar('Ord', int, float, str)

def partition(a: List[Ord], l: int, r: int) -> int:
    """ first element pivot """
    p = a[l]
    i = l + 1
    for j in range(l+1, r):
        if a[j] < p:
            a[j], a[i] = a[i], a[j]
            i += 1
    a[l], a[i-1] = a[i-1], a[l]

    return i-1

def quickSort(arr: List[Ord], l: int = 0, r: int = None):
    if r == None:
        r = len(arr)
    if l >= r:
        return
    p = partition(arr, l, r)
    quickSort(arr, l, p)
    quickSort(arr, p+1, r)

def quickSortOuter(data: List[Ord]) -> List[Ord]:
    quickSort(data)
    return data

if __name__ == '__main__':
    a = [8,3,4,6,2,5,7,1]
    print(quickSortOuter(a))

