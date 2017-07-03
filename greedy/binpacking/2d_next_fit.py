#!/usr/bin/env python
"""
2 dimensional Next Fit bin packing


"""

from collections import namedtuple
from typing import NamedTuple
from avl_tree import AvlTree, Node, traverse


class Item(NamedTuple):
    x: int
    y: int

class BinTree:
    """
    Tree data structure for holding the contents of a
    2 dimension bin.
    """
    def __init__(self, x: int = 4, y: int = 8, occupied: bool = False) -> None:
        self.x = x
        self.y = y
        self.occupied = occupied
        self.parent = None
        self.right = None
        self.bottom = None


    def insert(self, item: Item) -> bool:
        """
        Recursive item insertion
        Takes an Item namedtuple
        Inserts recursively as a side-effect
        Returns True or False if Item fit in bin
        """
        if item.y <= self.y:
            if self.occupied is False:
                if self.y - item.y > 0:
                    self.bottom = BinTree(x=self.x, y=self.y-item.y)
                if self.x - item.x > 0:
                    self.right = BinTree(x=self.x-item.x, y=item.y)
                self.y, self.x = item.y, item.x
                self.occupied = True
                return True
            else:
                if self.right.x >= item.x:
                    self.right.insert(item)
                elif self.bottom.y >= item.y:
                    self.bottom.insert(item)
                else:
                    return False

def nodeState(node: BinTree) -> None:
    print('x: %s,  y: %s' % (node.x, node.y))
    print('Node %s occupied' % ('is' if node.occupied else 'is not'))
    print('Node right child: %s' % (True if node.right else False))
    print('Node bottom child: %s' % (True if node.bottom else False))


if __name__ == '__main__':
    root = BinTree()
    item1 = Item(x=2, y=4)
    item2 = Item(x=4, y=4)
    item3 = Item(x=2, y=2)
    root.insert(item1)
    root.insert(item2)
    root.insert(item3)
    print("root")
    nodeState(root)
    print("")
    print("root.right")
    nodeState(root.right)
    print("")
    print("root.bottom")
    nodeState(root.bottom)
    print("")
