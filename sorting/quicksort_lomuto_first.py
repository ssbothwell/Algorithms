#!/usr/bin/env python
"""
Lomuto's Quicksort Algorithm
First Element Pivot

Performance:
    Worst case: O(n^2)
    Best case: O(nlogn)
    Average: O(nlogn)
"""
from typing import List, TypeVar
Ord = TypeVar('Ord', int, float, str)

def partition(arr: List[Ord], left: int, right: int) -> int:
    """ first element pivot """
    pivot = arr[left]
    i = left + 1
    for j in range(left+1, right):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[left], arr[i-1] = arr[i-1], arr[left]

    return i-1

def quick_sort(arr: List[Ord], left: int = 0, right: int = None):
    if right is None:
        right = len(arr)
    if left >= right:
        return
    pivot = partition(arr, left, right)
    quick_sort(arr, left, pivot)
    quick_sort(arr, pivot+1, right)

def quick_sort_outer(data: List[Ord]) -> List[Ord]:
    """ quick_sort() wrapper """
    quick_sort(data)
    return data

if __name__ == '__main__':
    unsorted_list = [8, 3, 4, 6, 2, 5, 7, 1]
    print(quick_sort_outer(unsorted_list))
