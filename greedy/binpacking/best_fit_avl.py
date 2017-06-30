#!/usr/bin/env python
"""
1 dimensional Best Fit bin packing with an AvlTree
"""

from collections import deque
from typing import List
from avl_tree import AvlTree, Node, traverse



class BestFitTree(AvlTree):
    """ subclass of AvlTree with bin packing specifics:
        -bin content dict for tracking items in bins.
        -Initializes with a single bin Node in place.
        -Update, Insert, and Search (best_fit()) methods
          for bin Nodes.
    """
    def __init__(self, bin_capacity: int) -> None:
        AvlTree.__init__(self)
        self.bin_size = bin_capacity
        self.root = Node(bin_capacity)
        self.root.data = [0]
        self.bin_contents = {0:[]} # Type: Dict[int,list]
        self.bin_count = 0

    def update_bin(self, old_bin: int, new_key: int) -> None:
        """ Update the bin's key after a new item has been added """
        if new_key is 0:
            old_bin.data.pop()
        else:
            duplicate_bin = self.get(new_key)
            if duplicate_bin:
                duplicate_bin.data += old_bin.data
                duplicate_bin.count += 1
            else:
                unique_bin = self.insert(new_key)
                if old_bin.count > 1:
                    unique_bin.data = old_bin.data[-1]
                    old_bin.data.pop()
                else:
                    unique_bin.data = old_bin.data
        self.delete(old_bin.key)

    def insert_item(self, item: int) -> None:
        """
        Call best_fit(), insert the item into a bin (or
        create a new bin and insert), and update
        bin_contents dict with new item
        """
        best_bin = self.best_fit(item)
        if best_bin:
            self.bin_contents[best_bin.data[-1]].append(item)
            new_capacity = best_bin.key - item
            self.update_bin(best_bin, new_capacity)
        else:
            self.bin_count += 1
            new_bin = self.insert(self.bin_size)
            new_bin.data = [self.bin_count]
            self.bin_contents[self.bin_count] = []
            self.insert_item(item)

    def best_fit(self, weight: int) -> Node:
        """
        Find the bin with the least capacity but still
        more then `weight`
        """
        best_bin = None
        search_queue = deque([self.root])
        while search_queue:
            bin_node = search_queue.popleft()
            if bin_node and bin_node.key == weight:
                best_bin = bin_node
                break
            elif bin_node and bin_node.key > weight:
                best_bin = bin_node
                if bin_node.left:
                    search_queue.append(bin_node.left)
            elif bin_node and bin_node.key < weight:
                if bin_node.right:
                    search_queue.append(bin_node.right)
        return best_bin


def avl_best_fit(item_list: List[int], bin_size: int) -> dict:
    """ Wrapper function for bin tree """
    tree = BestFitTree(bin_size)
    for item in item_list[:]:
        tree.insert_item(item)
    if tree.root:
        traverse(tree.root)
    return tree.bin_contents


if __name__ == '__main__':
    ITEMS = sorted([1, 4, 9, 4, 1, 5, 8, 3, 2, 5, 7, 3, 2, 6], reverse=True)
    print(avl_best_fit(ITEMS, 10))
