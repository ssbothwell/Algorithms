#!/usr/bin/env python
from typing import Dict, Tuple, List

"""
Best Fit Bin Packing

1. Try to place the item in the fullest bin that will accommodate it, i.e., the bin that will leave the least room left over
2. If no bin is found, start a new bin

"""

def best_fit(b_size: int, item_list: List[int]) -> Tuple[int, dict]:
    # Bin Count
    bin_count = 1
    # List of remaining capacities for each bin
    bin_capacity = [b_size] * len(item_list)
    # Bin Contents
    bins = { x: [] for x in range(len(item_list))} # type: Dict[int, list]

    for item_index, item in enumerate(item_list):
        best_bin = None
        best_weight = b_size + 1
        for bin_index in range(bin_count):
            if bin_capacity[bin_index] >= item and \
                    bin_capacity[bin_index] - item < best_weight:
                best_weight = bin_capacity[bin_index] - item
                best_bin = bin_index
        if best_weight == b_size + 1:
            bin_capacity[bin_count] = b_size - item
            bins[bin_count].append(item_index)
            bin_count += 1
        else:
            bin_capacity[best_bin] -= item
            bins[best_bin].append(item_index)

    return bin_count, { k: v for k, v in bins.items() if len(v) > 0 }


if  __name__ == '__main__':
    sizes = [1, 4, 9, 4, 1, 5, 8, 3, 2, 5, 7, 3, 2, 6]
    num_items = len(sizes)
    bin_size = 10

    bins_used, bins = best_fit(bin_size, sizes)
    print("%s bins were used" % bins_used)
    print(bins)
