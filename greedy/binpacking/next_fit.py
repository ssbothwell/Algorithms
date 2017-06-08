#!/usr/bin/env python
from typing import Dict, List

"""
Next Fit Bin Packing

1. Place each item in a single bin until an item will not fit
2. When an item won’t fit, close that bin and begin another

"""

def next_fit(b_size: int , items: List[int]) -> Dict[int,list]:
    current_bin = 0
    capacity = b_size
    # Bin Contents
    bins = { x: [] for x in range(len(items))} # type: Dict[int, list]
    for i in range(0, len(items)):
        if (items[i] > capacity):
            current_bin += 1
            capacity = b_size
        capacity -= sizes[i]
        bins[current_bin].append(i)
    return { k: v for k, v in bins.items() if len(v) > 0 }

def print_results(item_list: List[int], bins: Dict[int, list]):
    for pair in bins.items():
        print("Bin #%s: %s" % pair)
    return

if  __name__ == '__main__':
    sizes = [1, 4, 9, 4, 1, 5, 8, 3, 2, 5, 7, 3, 2, 6]
    bin_size = 10

    bins = next_fit(bin_size, sizes)
    print_results(sizes, bins)
