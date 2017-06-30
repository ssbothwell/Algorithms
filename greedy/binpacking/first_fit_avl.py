#!/usr/bin/env python
from typing import Dict, Tuple, List
from avl_tree import AvlTree, Node

"""
First Fit Bin Packing

1. Try to place the item in the first bin that will accommodate it
2. If no bin is found, start a new bin

"""

class bin_tree(AvlTree):
    def next_search(self, item_size):
        """ Returns lowest key greater then item_size"""
        if self.root:
            res = self._next_search(key,self.root)
            if res:
                return res
            else:
                return None
        else:
            return None

    def _next_search(self, item_size, current_node):
        """ Recursive next_search inner function """
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._next_search(key, current_node.left)
        else:
            return self._next_search(key,current_node.right)


def first_fit(b_size: int, item_list: List[int]) -> Dict[int, list]:
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

    return { k: v for k, v in bins.items() if len(v) > 0 }

def print_results(item_list: List[int], bins: Dict[int, list]):
    for pair in bins.items():
        print("Bin #%s: %s" % pair)
    return

if  __name__ == '__main__':
    sizes = [1, 4, 9, 4, 1, 5, 8, 3, 2, 5, 7, 3, 2, 6]
    num_items = len(sizes)
    bin_size = 10

    bins = first_fit(bin_size, sizes)
    print(bins)
    #print_results(sizes, bins)
