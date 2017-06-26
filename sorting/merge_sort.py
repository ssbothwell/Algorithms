#!/usr/bin/env python
from typing import List, TypeVar
Ord = TypeVar('Ord', int, float, str)

def mergeSort(arr: List[Ord]) -> List[Ord]:
    """ Takes an unsorted list of orderables and returns
    an ordered list """
    if len(arr) == 1:
        return arr
    else:
        left = arr[:len(arr)//2]
        right = arr[len(arr)//2:]

        left = mergeSort(left)
        right = mergeSort(right)
        merged_list = []

        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged_list.append(left[i])
                i = i + 1
            else:
                merged_list.append(right[j])
                j = j + 1

        merged_list += left[i:]
        merged_list += right[j:]

        return merged_list

if __name__ == '__main__':
    unsorted_list = [2, 4, 6, 8, 3]
    print(mergeSort(unsorted_list))
