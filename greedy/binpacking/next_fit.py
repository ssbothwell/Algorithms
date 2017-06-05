#!/usr/bin/env python
import sys
"""
Next Fit Bin Packing

"""

def next_fit(b_size, sizes, bins, n_items):
    current_bin = 0
    capacity = b_size
    for i in range(0, n_items):
        if (sizes[i] > capacity):
            current_bin += 1
            capacity = b_size
        capacity -= sizes[i]
        bins[current_bin].append(sizes[i])
    return current_bin + 1


if  __name__ == '__main__':
    sizes = [1, 4, 9, 4, 1, 5, 8, 3, 2, 5, 7, 3, 2, 6]
    num_items = len(sizes)
    bin_size = 10
    bins = { x: [] for x in range(num_items)}

    bins_used = next_fit(bin_size, sizes, bins, num_items)
    print("%s bins were used" % bins_used)
    print(bins)
