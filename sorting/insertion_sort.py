#!/usr/bin/env python
"""
Insertion Sort
O(n^2) Worst Case Performance

An in-place comparison-based sorting algorithm similar
to how a person sorts a hand of playing cards. A subarray
of sorted elements is grown through an iterative process.

At each position in the array (starting from index 1), the
value is checked against the highest value in the sorted
subarray. If the new value is greater, it is left where it
is otherwise it is checked successively against lower indices
in the sorted subarray until the correct position for it
is found.
"""
from typing import List, TypeVar
Ord = TypeVar('Ord', int, float, str)

def insertion_sort(arr: List[Ord]) -> List[Ord]:
    """ takes an unsorted list of orderable elements
    returns an ordered list """
    for i, _ in enumerate(arr):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j = j - 1
    return arr


if __name__ == '__main__':
    unsorted_list = [2, 1, 4, 5, 6, 8, 3]
    print(insertion_sort(unsorted_list))
