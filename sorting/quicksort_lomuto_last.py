#!/usr/bin/env python
"""
Lomuto's Quicksort Algorithm
Last Element Pivot

Performance:
    Worst case: O(n^2)
    Best case: O(nlogn)
    Average: O(nlogn)
"""
from typing import List, TypeVar
Ord = TypeVar('Ord', int, float, str)

def partition(arr: List[Ord], left: int, right: int) -> int:
    """ final element pivot """
    pivot = arr[right-1]
    i = left - 1
    for j in range(left, right-1):
        if arr[j] <= pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[right-1], arr[i+1] = arr[i+1], arr[right-1]

    return i+1

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
