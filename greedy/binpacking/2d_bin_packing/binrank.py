#!/usr/bin/env python
"""
Bin Ranking Tree

An AVL Tree implementation used to order BinTree. Each
Bintree is associated with an AVL node. Order is by max
unoccupied BinTree node.

BinTrees and corresponding IDs are stored in a dict. AVL
Node payloads hold IDs and Node keys are the BinTree's max
unoccupied scores.
"""

from ../avl_tree import AvlTree, Node, traverse

class BinRank:
    def __init__(self):
        self.bin_dict = {}
        pass


    def _add_bin(self) -> None:
        pass


    def pick_bin(self, item_dims: tuple) -> int:
        pass




if __name__ == '__main__':
    pass
