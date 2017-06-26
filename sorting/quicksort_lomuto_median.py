#!/usr/bin/env python
"""
Lomuto's Quicksort Algorithm
Median of Three Pivot

Performance:
    Worst case: O(n^2)
    Best case: O(nlogn)
    Average: O(nlogn)
"""
from typing import List, TypeVar
Num = TypeVar('Num', int, float)

def partition(array: List[Num], start: int, end: int) -> int:
    """ median of three partition """
    median = (end -1 - start) // 2
    median = median + start
    left = start + 1
    if (array[median] - array[end-1])*(array[start]-array[median]) >= 0:
        array[start], array[median] = array[median], array[start]
    elif (array[end - 1] - array[median]) * (array[start] - array[end - 1]) >= 0:
        array[start], array[end-1] = array[end-1], array[start]
    pivot = array[start]
    for right in range(start, end):
        if pivot > array[right]:
            array[left], array[right] = array[right], array[left]
            left = left + 1
    array[start], array[left-1] = array[left-1], array[start]
    return left-1

def quick_sort(arr: List[Num], left: int = 0, right: int = None) -> None:
    if right is None:
        right = len(arr)
    if left >= right:
        return
    pivot = partition(arr, left, right)
    quick_sort(arr, left, pivot)
    quick_sort(arr, pivot+1, right)

def quick_sort_outer(data: List[Num]) -> List[Num]:
    """ quick_sort() wrapper """
    quick_sort(data)
    return data

if __name__ == '__main__':
    unsorted_list = [8, 3, 4, 6, 2, 5, 7, 1]
    print(quick_sort_outer(unsorted_list))
