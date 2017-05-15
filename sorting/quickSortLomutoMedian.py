#!/usr/bin/env python
from typing import List, TypeVar
Num = TypeVar('Num', int, float)

def partition(array: List[Num], start: int, end: int) -> int:
    """ median of three """
    median = (end -1 - start) // 2
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

def quickSort(arr: List[Num], l: int = 0, r: int = None) -> None:
    if r == None:
        r = len(arr)
    if l >= r:
        return
    p = partition(arr, l, r)
    quickSort(arr, l, p)
    quickSort(arr, p+1, r)

def quickSortOuter(data: List[Num]) -> List[Num]:
    quickSort(data)
    return data

if __name__ == '__main__':
    a = [8,3,4,6,2,5,7,1]
    print(quickSortOuter(a))
