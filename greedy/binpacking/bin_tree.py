#!/usr/bin/env python
from collections import deque
from typing import Dict, Tuple, List
from avl_tree import AVL_Tree, Node, traverse

"""
AVL_Tree subclass for storing bins

"""


class bin_tree(AVL_Tree):
    def __init__(self, bin_capacity: int, items: List[int]):
        AVL_Tree.__init__(self)
        self.bin_size = bin_capacity
        self.root = Node(bin_capacity)
        self.root.payload = 0
        self.bin_contents = {0:[]}
        self.bin_count = 0

    def update_bin(self, current_key: int, new_key: int):
        node = self.get(current_key)
        new_node = self.get(new_key)

        self.insert(new_key, payload=node.payload)
        self.delete(current_key)


    def insert_item(self, item: int):
        best_fit_bin = self.best_fit(item)
        # If the item fits a bin
        if best_fit_bin:
            best_bin = self.get(best_fit_bin)
            # add item to bin contents hash
            self.bin_contents[best_bin.payload].append(item)
            # delete and reinsert bin to update key (capacity)
            self.update_bin(best_bin.key, best_bin.key-item)
            #bb_key = best_bin.key
            #bb_payload = best_bin.payload
            #self.delete(best_bin.key)
            #self.insert(bb_key-item, payload=bb_payload)

        # Create a new bin and try again
        else:
            self.bin_count += 1
            self.insert(self.bin_size, payload=self.bin_count)
            self.bin_contents[self.bin_count] = []
            self.insert_item(item)

    def best_fit(self, weight: int):
        """ find the node with the lowest capacity higher then `weight` """

        best_bin = None
        search_queue = deque()
        search_queue.append(self.root)
        while len(search_queue) != 0:
            n = search_queue.popleft()
            if n.key == weight:
                best_bin = n.key
                break
            elif n.key > weight:
                best_bin = n.key
                if n.left:
                    search_queue.append(n.left)
            elif n.key < weight:
                if n.right:
                    search_queue.append(n.right)
        return best_bin

if __name__ == '__main__':
    items = [1, 4, 9, 4, 1, 5, 8, 3, 2, 5, 7, 3, 2, 6]
    tree = bin_tree(10, items)
    tree.insert(12)
    tree.delete(10)
    #for item in items[:1]:
    #    tree.insert_item(item)
    #print(tree.bin_contents)
    #traverse(tree.root)
    print(tree.root)
