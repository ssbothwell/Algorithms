#!/usr/bin/env python
from typing import List, TypeVar
Ord = TypeVar('Ord', int, float, str)

def selSort(arr: List[Ord]) -> List[Ord]:
    for i in range(len(arr)-1,0,-1):
        # Temporary storage for index of highest element
        maxIndex = 0
        # Iterate from index 0 to index i inclusive
        for j in range(0, i+1):
            # Find highest value index
            if arr[j] > arr[maxIndex]:
                maxIndex = j

        # Store element to be swapped out
        temp = arr[i]
        # Swap the two elements
        arr[i], arr[maxIndex]  = arr[maxIndex], temp
    return arr

if __name__ == '__main__':
    a = [8,3,4,6,2,5,7,1]
    print(selSort(a))
