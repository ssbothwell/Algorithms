#!/usr/bin/env python

"""
Class based binary search tree.
Source: https://interactivepython.org/runestone/static/pythonds/Trees/SearchTreeImplementation.html

A tree constists of a single binary_search_tree object and
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
class binary_search_tree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        """
        initial put() method.
        If a root node exists, call recursive _put() method
        with the root node as current selected node (currentNode).
        Otherwise create root node with key,val from put().
        """
        if self.root:
            # if tree has a root call the recursive _put() function
            self._put(key, val, self.root)
        else:
            # else create root
            self.root = tree_node(key, val)
        # update tree size
        self.size += 1

    def _put(self, key, val, currentNode):
        """
        Recursive put() method.
        Checks if new key is greater or less then currently
        selected node. If less it recurses on the left_child
        otherwise it recurses on the right_child.
        """
        if key < currentNode.key:
            if currentNode.has_left_child():
                self._put(key, val, currentNode.left_child)
            else:
                currentNode.left_child = tree_node(key, val, parent=currentNode)
        else:
            if currentNode.has_right_child():
                self._put(key, val, currentNode.right_child)
            else:
                currentNode.right_child = tree_node(key, val, parent=currentNode)

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

    def delete(self, key):
        """ Finds the node to delete then calls the remove() method """
        if self.size > 1:
            # search for node to delete
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and key == self.root.key:
            self.root = None
            self.size = 0
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, currentNode):
        """
        When removing a node there are three cases:
            1. The node has no children:
                Delete pointer in parent node and
                delete node object.
            2. The node has one child:
                Promote the child to take node's place
                then delete node object.
            3. The node has two children:
                Search tree for a node that can replace
                the node and preserve the binary structure
                This will be the next largest node in
                the tree and will never have two children.
                This means it can be removed and swapped
                in using the first two cases.
        """

        # Node has no children
        if currentNode.is_leaf():
            if currentNode == currentNode.parent.left_child:
                currentNode.parent.left_child = None
            else:
                currentNode.parent.right_child = None
        # Node has both children
        elif currentNode.has_both_children():
            succ = currentNode.find_successor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        # Node has one child
        else:
            if currentNode.has_left_child():
                if currentNode.is_left_child():
                    currentNode.left_child.parent = currentNode.parent
                    currentNode.parent.left_child = currentNode.left_child
                elif currentNode.is_right_child():
                    currentNode.left_child.parent = currentNode.parent
                    currentNode.parent.right_child = currentNode.left_child
                else:
                    # currentNode is root then swap data with child
                    currentNode.replace_node_data(
                                    currentNode.left_child.key,
                                    currentNode.left_child.payload,
                                    currentNode.left_child.left_child,
                                    currentNode.left_child.right_child)
            elif currentNode.has_right_child():
                if currentNode.is_left_child():
                    currentNode.right_child.parent = currentNode.parent
                    currentNode.parent.left_child = currentNode.right_child
                elif currentNode.is_right_child():
                    currentNode.right_child.parent = currentNode.parent
                    currentNode.parent.right_child = currentNode.right_child
                else:
                    # currentNode is root then swap data with child
                    currentNode.replace_node_data(
                                    currentNode.right_child.key,
                                    currentNode.right_child.payload,
                                    currentNode.right_child.left_child,
                                    currentNode.right_child.right_child)



class tree_node:

    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.payload = val
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

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

    def has_any_children(self):
        """ True if node  has any children """
        return self.left_child or self.right_child

    def has_both_children(self):
        return self.left_child and self.right_child

    def replace_node_data(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.left_child = lc
        self.right_child = rc
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self

    def find_successor(self):
        """
        Find the next largest node after the node to be deleted

        If the node has a right child, the successor will be the
        smallest node on the right sub tree.

        If the node has no right child and is the left child of
        a parent node then the parent is the successor

        If the node has no right child, and is the righ child of
        it's parent then the successor is the successor to its
        parent.
        """
        succ = None
        if self.has_right_child():
            succ = self.right_child.find_min()
        else:
            if self.parent:
                if self.is_left_child():
                    succ = self.parent
                else:
                    self.parent.right_child = None
                    succ = self.parent.find_successor()
                    self.parent.right_child = self

        return succ

    def find_min(self):
        current = self
        while current.has_left_child():
            current = current.left_child
        return current

    def splice_out(self):
        # if has null children
        if self.is_leaf():
            # Remove node from parent association
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.has_any_children():
            if self.has_left_child:
                # if has a chikd then link parent to child
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent

    def __iter__(self):
        if self:
            if self.has_left_child():
                for elem in self.left_child:
                    yield elem
                yield self.key
            if self.has_right_child():
                for elem in self.right_child:
                    yield elem


if __name__ == '__main__':
    tree = binary_search_tree()
    tree[70] = 70
    tree[31] = 31
    tree[93] = 93
    tree[14] = 14
    tree[73] = 73
    tree[94] = 94
    tree[23] = 23

    def traverse(node, level=0):
        level += 1
        if node.has_any_children() == None:
            return node.key, level
        else:
            l,r = None, None
            if node.left_child != None:
                l = traverse(node.left_child,level)
            if node.right_child != None:
                r = traverse(node.right_child,level)
            if l and r:
                print l,r
            if l and not r:
                print l
            if r and not l:
                print r
            return node.key, level

    print traverse(tree.root)
