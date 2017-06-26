#!/usr/bin/env python
from typing import List, TypeVar, Tuple
Ord = TypeVar('Ord', int, float, str)

def mergeSortInv(arr: List[Ord]) -> Tuple[List[Ord], int]:
    if len(arr) == 1:
        return arr, 0
    else:
        left = arr[:len(arr)//2]
        right = arr[len(arr)//2:]

        left, left_inversions = mergeSortInv(left)
        right, right_inversions = mergeSortInv(right)
        merge_list = []

        i = 0
        j = 0
        inversions = 0 + left_inversions + right_inversions

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merge_list.append(left[i])
                i += 1
            else:
                merge_list.append(right[j])
                j += 1
                inversions += (len(left)-i)

        merge_list += left[i:]
        merge_list += right[j:]

        return merge_list, inversions

if __name__ == '__main__':
    unsorted_list = [2, 4, 6, 8, 3]
    print(mergeSortInv(unsorted_list))
