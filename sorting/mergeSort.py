#!/usr/bin/env python
from typing import List, TypeVar
Ord = TypeVar('Ord', int, float, str)

def mergeSort(arr: List[Ord]) -> List[Ord]:
    if len(arr) == 1:
        return arr
    else:
        a = arr[:len(arr)//2]
        b = arr[len(arr)//2:]

        a = mergeSort(a)
        b = mergeSort(b)
        c = []

        i = 0
        j = 0

        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                c.append(a[i])
                i = i + 1
            else:
                c.append(b[j])
                j = j + 1

        c += a[i:]
        c += b[j:]

        return c

if __name__ == '__main__':
    arr = [2,4,6,8,3]
    print(mergeSort(arr))
