#!/usr/bin/env python
from typing import Dict, Tuple, List

"""
Worst Fit Bin Packing

1. Try to place the item in the least full bin that will accommodate
   it, i.e., bin that will leave the most room left over
2. If no bin is found, start a new bin

"""

def worst_fit(b_size: int, item_list: List[int]) -> Dict[int, List]:
    # Bin Count
    bin_count = 0
    # List of remaining capacities for each bin
    bin_capacity = [b_size] * len(item_list)
    # Bin Contents
    bins = { x: [] for x in range(len(item_list))} # type: Dict[int, list]

    for item_index, item in enumerate(item_list):
        best_bin = 0
        best_weight = bin_capacity[best_bin]
        fit = False
        for bin_index in range(bin_count):
            if bin_capacity[bin_index] >= item and \
                    bin_capacity[bin_index] - item >= best_weight - item:
                best_weight = bin_capacity[bin_index] - item
                best_bin = bin_index
                fit = True
        if fit == False:
            bin_capacity[bin_count] = b_size - item
            bins[bin_count].append(item_index)
            bin_count += 1
        else:
            bin_capacity[best_bin] -= item
            bins[best_bin].append(item_index)

    return { k: v for k, v in bins.items() if len(v) > 0 }

def print_results(item_list: List[int], bins: Dict[int, list]):
    for pair in bins.items():
        print("Bin #%s: %s" % pair)
    return

if  __name__ == '__main__':
    sizes = [1, 4, 9, 4, 1, 5, 8, 3, 2, 5, 7, 3, 2, 6]
    num_items = len(sizes)
    bin_size = 10

    bins = worst_fit(bin_size, sizes)
    print_results(sizes, bins)

