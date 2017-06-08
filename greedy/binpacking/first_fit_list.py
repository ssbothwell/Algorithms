#!/usr/bin/env python
from typing import Dict, Tuple, List

"""
First Fit Bin Packing

1. Try to place the item in the first bin that will accommodate it
2. If no bin is found, start a new bin

"""

def first_fit(b_size: int, item_list: List[int]) -> Tuple[int, dict]:
    # Bin Count
    bin_count = 1
    # List of remaining capacities for each bin
    bin_capacity = [b_size] * bin_count
    # Bin Contents
    bins = { x: [] for x in range(len(item_list))} # type: Dict[int, list]

    for item_index, item in enumerate(item_list):
        for bin_index in range(bin_count):
            if bin_capacity[bin_index] >= item:
                bin_capacity[bin_index] -= item
                bins[bin_index].append(item_index)
                break
        # If no bin could fit item, increment bin count
        if bin_index == bin_count - 1:
            bin_count += 1
            bin_capacity.append(10)

    return bin_count-1, { k: v for k, v in bins.items() if len(v) > 0 }


if  __name__ == '__main__':
    sizes = [1, 4, 9, 4, 1, 5, 8, 3, 2, 5, 7, 3, 2, 6]
    num_items = len(sizes)
    bin_size = 10

    bins_used, bins = first_fit(bin_size, sizes)
    print("%s bins were used" % bins_used)
    print(bins)
