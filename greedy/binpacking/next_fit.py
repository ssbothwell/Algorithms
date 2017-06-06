#!/usr/bin/env python
from typing import Dict, Tuple, List

"""
Next Fit Bin Packing

1. Place each item in a single bin until an item will not fit
2. When an item won’t fit, close that bin and begin another

"""

def next_fit(b_size: int , items: List[int], bins: Dict[int, List[int]]) -> int:
    current_bin = 0
    capacity = b_size
    for i in range(0, len(items)):
        if (items[i] > capacity):
            current_bin += 1
            capacity = b_size
        capacity -= sizes[i]
        bins[current_bin].append(sizes[i])
    return current_bin + 1


if  __name__ == '__main__':
    sizes = [1, 4, 9, 4, 1, 5, 8, 3, 2, 5, 7, 3, 2, 6]
    bin_size = 10
    bins = { x: [] for x in range(len(sizes))} # type: Dict[int, list] 

    bins_used = next_fit(bin_size, sizes, bins)
    print("%s bins were used" % bins_used)
    print({ k: v for k, v in bins.items() if len(v) > 0 })
