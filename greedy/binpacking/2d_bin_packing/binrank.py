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
import avl_tree, bintree

class BinRank:
    """
    Bin Ranking System. the product of BinTree.largest_child
    is used as a key value in an AVL Tree for ranking the bins.
    """
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


    def best_fit(self, item_dims: tuple) -> bool:
        """
        First Fit Bin Selection
        Public method.
        Selects optimal BinTree (or creates
        a new BinTree) for item insertion using first fit.
        Returns BinTree ID.
        """
        item_area = product(*item_dims)
        item = bintree.Item(*item_dims)
        queue = deque([self.tree.root])
        best_fit = None
        best_fit_node = None
        while queue:
            current_node = queue.popleft()
            current_bintree = self.bin_dict[current_node.data[-1]]
            if current_node.key >= item_area:
                largest_child = current_bintree.largest_child
                if (largest_child[0] >= item.width and
                        largest_child[1] >= item.height):
                    if not best_fit or largest_child < best_fit.largest_child:
                        best_fit = current_bintree
                        best_fit_node = current_node
                if current_node.left:
                    queue.append(current_node.left)
            else:
                if current_node.right:
                    queue.append(current_node.right)
        if best_fit:
            best_fit.insert(item)
            # delete and reinsert node to update position in tree
            nodeid = best_fit_node.data[-1]
            old_key = best_fit_node.key
            new_key = product(*best_fit.largest_child)
            self.tree.delete(key=old_key)
            self.tree.insert(key=new_key)
            self.tree[new_key].data.append(nodeid)
            return True
        else:
            self._add_bin()
            self.bin_dict[self.bin_count-1].insert(item)
            return True


    def next_fit(self, item_dims: tuple) -> bool:
        """
        First Fit Bin Selection
        Public method.
        Selects optimal BinTree (or creates
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
                    self.next_fit(item_dims)
        return False


    def print_layouts(self) -> None:
        """
        Returns layouts for all BinTrees
        """
        for key, bin in self.bin_dict.items():
            bin.print_layout()

if __name__ == '__main__':
    BRANK = BinRank()
    BRANK.best_fit((2, 4))
    BRANK.best_fit((2, 2))
    BRANK.best_fit((4, 5))
    BRANK.best_fit((4, 4))
    BRANK.best_fit((2, 2))
    avl_tree.traverse(BRANK.tree.root)
    BRANK.print_layouts()
