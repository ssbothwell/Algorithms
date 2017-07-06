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
        self.tree = AvlTree()


    def _add_bin(self) -> None:
        """
        private method. Creates a new BinTree and adds
        it to bin_dict and the AVL tree.
        """
        pass


    def pick_bin(self, item_dims: tuple) -> int:
        """
        public method. Selects optimal BinTree (or creates
        a new BinTree) for item insertion.
        Returns BinTre ID.
        """
        pass


    def print_layouts(self):
        """
        Returns layouts for all BinTrees
        """
        pass


if __name__ == '__main__':
    pass
