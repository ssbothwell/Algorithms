#!/usr/bin/env python

"""
Class based AVL balanced binary search tree.
Source: https://interactivepython.org/runestone/static/pythonds/Trees/AVLTreeImplementation.html

A tree constists of a single avl_tree object and
many tree_node objects.

The binary_search_tree object stores a pointer to the
root node, a value for the length of the tree (number of
nodes), and methods for length(), put(), get(), delete(),
some helper methods.

tree_node objects store a key, a data value, and pointers
parent and left/right child nodes. They also have some
helper methods to assist with the main binary_search_tree
methods.
"""

class AVL_tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key):
        """
        initial put() method.
        If a root node exists, call recursive _put() method
        with the root node as current selected node (currentNode).
        Otherwise create root node with key,val from put().
        """
        if self.root:
            # if tree has a root call the recursive _put() function
            self._put(key, self.root)
        else:
            # else create root
            self.root = Node(key)
        # update tree size
        self.size += 1

    def _put(self,key,currentNode):
        """
        Recursive put() method.
        Checks if new key is greater or less then currently
        selected node. If less it recurses on the left_child
        otherwise it recurses on the right_child.
        """
        if key < currentNode.key:
            if currentNode.has_left_child():
                    self._put(key,currentNode.left_child)
            else:
                    currentNode.left_child = Node(key,parent=currentNode)
                    self.updateBalance(currentNode.left_child)
        else:
            if currentNode.has_right_child():
                    self._put(key,currentNode.right_child)
            else:
                    currentNode.right_child = Node(key,parent=currentNode)
                    self.updateBalance(currentNode.right_child)

    def updateBalance(self, node):
        """
        checks to see if the current node is out of balance enough
        to require rebalancing.
        """
        if node.balance_factor > 1 or node.balance_factor < -1:
            self.rebalance(node)
            return
        if node.parent != None:
            if node.is_left_child():
                    node.parent.balance_factor += 1
            elif node.is_right_child():
                    node.parent.balance_factor -= 1

            if node.parent.balance_factor != 0:
                    self.updateBalance(node.parent)

    def rebalance(self, node):
      if node.balance_factor < 0:
             if node.right_child.balance_factor > 0:
                self.__right_rotate(node.right_child)
                self.__left_rotate(node)
             else:
                self.__left_rotate(node)
      elif node.balance_factor > 0:
             if node.left_child.balance_factor < 0:
                self.__left_rotate(node.left_child)
                self.__right_rotate(node)
             else:
                self.__right_rotate(node)

    def __left_rotate(self, rotRoot):
        newRoot = rotRoot.right_child
        rotRoot.right_child = newRoot.left_child
        if newRoot.left_child != None:
            newRoot.left_child.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.is_root():
            self.root = newRoot
        else:
            if rotRoot.is_left_child():
                    rotRoot.parent.left_child = newRoot
            else:
                rotRoot.parent.right_child = newRoot
        newRoot.left_child = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balance_factor = rotRoot.balance_factor + 1 - min(newRoot.balance_factor, 0)
        newRoot.balance_factor = newRoot.balance_factor + 1 + max(rotRoot.balance_factor, 0)

    def __right_rotate(self, rotRoot):
        newRoot = rotRoot.left_child
        rotRoot.left_child = newRoot.right_child
        if newRoot.right_child != None:
            newRoot.right_child.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.is_root():
            self.root = newRoot
        else:
            if rotRoot.is_left_child():
                    rotRoot.parent.left_child = newRoot
            else:
                rotRoot.parent.right_child = newRoot
        newRoot.right_child = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balance_factor = rotRoot.balance_factor + 1 - min(newRoot.balance_factor, 0)
        newRoot.balance_factor = newRoot.balance_factor + 1 + max(rotRoot.balance_factor, 0)

    def __setitem__(self, key, val):
        """ overloads the [] setter to use the put() method """
        self.put(key,val)

    def get(self, key):
        if self.root:
            res = self._get(key,self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.left_child)
        else:
            return self._get(key,currentNode.right_child)

    def __getitem__(self,key):
        """ Overloads [] getter to use get() """
        return self.get(key)

    def __contains__(self,key):
        """ Overloads `in` operator """
        if self._get(key, self.root):
            return True
        else:
            return False


class Node:
    def __init__(self, key, height=1, left_child=None, right_child=None, parent=None):
        self.key = key
        self.height = height
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent
        self.balance_factor = 0

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def has_any_children(self):
        """ True if node  has any children """
        return self.left_child or self.right_child

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        """ True if node has no parent """
        return not self.parent

    def is_leaf(self):
        """ True if node has no children """
        return not (self.left_child or self.right_child)

    def has_both_children(self):
        return self.left_child and self.right_child

    def __iter__(self):
        if self:
            if self.has_left_child():
                for elem in self.left_child:
                    yield elem
                yield self.key
            if self.has_right_child():
                for elem in self.right_child:
                    yield elem


def traverse(rootnode):
    thislevel = [rootnode]
    while thislevel:
        nextlevel = list()
        row_string = ""
        for n in thislevel:
            row_string += str(n.key) + " "
            if n.left_child: nextlevel.append(n.left_child)
            if n.right_child: nextlevel.append(n.right_child)
        print(row_string)
        thislevel = nextlevel

if __name__ == '__main__':
    tree = AVL_tree()
    tree.put(10)
    tree.put(20)
    tree.put(30)
    tree.put(40)
    tree.put(50)
    tree.put(25)

    traverse(tree.root)

