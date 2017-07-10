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
from collections import deque
from operator import mul as product
import avl_tree
import bintree

class BinRank:
    def __init__(self):
        self.bin_dict = {}
        self.tree = avl_tree.AvlTree()
        self.bin_count = 0
        self._add_bin()


    def _add_bin(self) -> None:
        """
        private method. Creates a new BinTree and adds
        it to bin_dict and the AVL tree.
        """
        self.bin_dict[self.bin_count] = bintree.BinTree()
        bin_key = product(*self.bin_dict[self.bin_count].largest_child)
        self.tree.insert(bin_key)
        self.tree[bin_key].data.append(self.bin_count)
        self.bin_count += 1


    def insert_item(self, item_dims: tuple) -> bool:
        """
        public method. Selects optimal BinTree (or creates
        a new BinTree) for item insertion using first fit.
        Returns BinTree ID.
        """
        item_area = product(*item_dims)
        item = bintree.Item(*item_dims)
        queue = deque([self.tree.root])
        while queue:
            current_node = queue.popleft()
            current_bintree = self.bin_dict[current_node.data[-1]]
            if current_node.key >= item_area:
                largest_child = current_bintree.largest_child
                if (largest_child[0] >= item.width and
                        largest_child[1] >= item.height):
                    current_bintree.insert(item)
                    # delete and reinsert node to update position in tree
                    nodeid = current_node.data[-1]
                    old_key = current_node.key
                    new_key = product(*current_bintree.largest_child)
                    self.tree.delete(key=old_key)
                    self.tree.insert(key=new_key)
                    self.tree[new_key].data.append(nodeid)
                    return True
            else:
                if current_node.right:
                    queue.append(current_node.right)
                else:
                    self._add_bin()
                    self.insert_item(item_dims)
        return False


    def print_layouts(self):
        """
        Returns layouts for all BinTrees
        """
        pass


if __name__ == '__main__':
    BRANK = BinRank()
    BRANK.insert_item((2,4))
    BRANK.insert_item((2,2))
    BRANK.insert_item((4,5))
    avl_tree.traverse(BRANK.tree.root)
    BRANK.bin_dict[0].print_layout()
    BRANK.bin_dict[1].print_layout()
