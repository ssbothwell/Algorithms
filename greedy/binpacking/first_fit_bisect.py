#!/usr/bin/env python
from typing import Dict, Tuple, List
from bisect import bisect_right

"""
First Fit Bin Packing

1. Try to place the item in the first bin that will accommodate it
2. If no bin is found, start a new bin

"""

def first_fit(b_size: int, item_list: List[int]) -> Dict[int,list]:
    # List of remaining capacities for each bin
    bin_capacity = [ [x, 10] for x in range(len(item_list))]
    # Bin Contents
    bins = { x: [] for x in range(len(item_list))} # type: Dict[int, list]

    for item_index, item in enumerate(item_list):
        bin_capacity = sorted(bin_capacity, key=lambda el: el[1])
        b_id, b_cap = zip(*bin_capacity)
        target_bin = bisect_right(b_cap, item)

        bin_capacity[target_bin][1] -= item
        bins[bin_capacity[target_bin][0]].append(item_index)

    return { k: v for k, v in bins.items() if len(v) > 0 }


if  __name__ == '__main__':
    sizes = [1, 4, 9, 4, 1, 5, 8, 3, 2, 5, 7, 3, 2, 6]
    num_items = len(sizes)
    bin_size = 10

    bins = first_fit(bin_size, sizes)
    #print("%s bins were used" % bins_used)
    print(bins)
