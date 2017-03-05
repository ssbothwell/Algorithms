#!/usr/bin/env python

def selSort(arr):
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

print selSort([4,5,1,3,2,7,9,11,0,13])

