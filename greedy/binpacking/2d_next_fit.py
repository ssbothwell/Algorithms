#!/usr/bin/env python

"""
2 dimensional Next Fit bin packing


"""

from typing import NamedTuple
#from avl_tree import AvlTree, Node, traverse

class CornerPoint(NamedTuple):
    """
    namedtuple representing the top left corner of each
    BinTree object
    """
    x: int
    y: int

class Item(NamedTuple):
    """
    namedtuple representing items placed in the bin.
    """
    width: int
    height: int

class BinTree:
    """
    Tree data structure for holding the contents of a
    2 dimension bin.
    """
    def __init__(self, width: int = 4, height: int = 8, occupied: bool = False, corner: CornerPoint = (0, 0)) -> None:
        self.corner = corner
        self.width = width
        self.height = height
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
        if item.height <= self.height:
            if self.occupied is False:
                if self.height - item.height > 0:
                    self.bottom = BinTree(width=self.width, height=self.height-item.height)
                    self.bottom.parent = self
                if self.width - item.width > 0:
                    self.right = BinTree(width=self.width-item.width, height=item.height)
                    self.right.parent = self
                self.height, self.width = item.height, item.width
                self.occupied = True
                if self.right:
                    self.right.corner = (self.width, self.corner[1])
                if self.bottom:
                    self.bottom.corner = (self.corner[0], self.height)
                return True
            else:
                if self.right.width >= item.width:
                    self.right.insert(item)
                elif self.bottom.height >= item.height:
                    self.bottom.insert(item)
                else:
                    return False

    def print_layout(self):
        """
        Returns bin layout in a renderable format
        """
        pass

def node_stage(node: BinTree) -> None:
    """
    Node Property Viewer
    """
    print('width: %s,  height: %s' % (node.width, node.height))
    print('position: %s, %s' % (node.corner))
    print('Node %s occupied' % ('is' if node.occupied else 'is not'))
    print('Node parent: %s' % (True if node.parent else False))
    print('Node right child: %s' % (True if node.right else False))
    print('Node bottom child: %s' % (True if node.bottom else False))


if __name__ == '__main__':
    ROOT = BinTree()
    ITEM1 = Item(width=2, height=4)
    ITEM2 = Item(width=4, height=4)
    ITEM3 = Item(width=2, height=2)
    ROOT.insert(ITEM1)
    ROOT.insert(ITEM2)
    ROOT.insert(ITEM3)
    print("ROOT")
    node_stage(ROOT)
    print("")
    print("ROOT.right")
    node_stage(ROOT.right)
    print("")
    print("ROOT.bottom")
    node_stage(ROOT.bottom)
    print("")
