#!/usr/bin/env python

def bubbleSort(arr):
    # Loop through list once per element
    for _ in range ( 0, len(arr)):
        for i in range(0, len(arr)-1):
            # compare and swap adjacent elements
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

