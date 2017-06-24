#!/usr/bin/env python
import time
from random import randint
from collections import deque
from typing import Dict, Tuple, List
from avl_tree import AVL_Tree, Node, traverse
from best_fit import *
from first_fit_bisect import *

"""
AVL_Tree subclass for storing bins

"""


class BinTree(AVL_Tree):
    def __init__(self, bin_capacity: int, items: List[int]) -> None:
        AVL_Tree.__init__(self)
        self.bin_size = bin_capacity
        self.root = Node(bin_capacity)
        self.root.payload = 0
        self.bin_contents = {0:[]} # Type: Dict[int,list]
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


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print( '%r  %2.2f ms' % \
                  (method.__name__, (te - ts) * 1000))
        return result
    return timed


@timeit
def avl_best_fit(items: List[int], bin_size: int) -> dict:
    tree = BinTree(bin_size, items)
    for item in items[:]:
        tree.insert_item(item)
    return tree.bin_contents


@timeit
def list_best_fit(items: List[int], bin_size: int) -> dict:
    return best_fit(bin_size, items)


@timeit
def bisect_first_fit(items: List[int], bin_size: int) -> dict:
    return first_fit(bin_size, items)


if __name__ == '__main__':
    items = [1, 4, 9, 4, 1, 5, 8, 3, 2, 5, 7, 3, 2, 6]
    items = [randint(1,10) for _ in range(10000)]
    avl_best_fit(items, 10)
    list_best_fit(items, 10)
    #bisect_first_fit(items, 10)
