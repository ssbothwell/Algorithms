#!/usr/bin/env python
from typing import List, TypeVar
Ord = TypeVar('Ord', int, float, str)

def sel_sort(arr: List[Ord]) -> List[Ord]:
    """ takes an unsorted list of orderable elements
    returns an ordered list """
    for i in range(len(arr)-1, 0, -1):
        # Temporary storage for index of highest element
        max_index = 0
        # Iterate from index 0 to index i inclusive
        for j in range(0, i+1):
            # Find highest value index
            if arr[j] > arr[max_index]:
                max_index = j

        # Swap the two elements
        arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr

if __name__ == '__main__':
    unsorted_list = [8, 3, 4, 6, 2, 5, 7, 1]
    print(sel_sort(unsorted_list))
