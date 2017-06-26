#!/usr/bin/env python
from typing import List, TypeVar
Ord = TypeVar('Ord', int, float, str)

def bubbleSort(arr: List[Ord]) -> List[Ord]:
    # Loop through list once per element
    for _ in range(0, len(arr)):
        for i in range(0, len(arr)-1):
            # compare and swap adjacent elements
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


if __name__ == '__main__':
    unsorted_list = [5, 3, 2, 4, 1]
    print(bubbleSort(unsorted_list))
