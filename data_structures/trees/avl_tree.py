#!/usr/bin/env python

"""
Class based AVL balanced binary search tree.
Based on designs from:
https://interactivepython.org/runestone/static/pythonds/Trees/AVLTreeImplementation.html
http://www.geeksforgeeks.org/avl-tree-set-2-deletion/

A tree constists of a single AVL_Tree object and
many Node objects.

What distinguises AVL_Tree from a plain Binary Search Tree is
it's self balancing property. Whenever a node is inserted or
deleted, the balance factors of the affected nodes are checked
and Nodes are rotated to maintain balance in the tree. This
ensures O(logN) insertion, deletion, and search performance.

"""

class Node:
    def __init__(self, key, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right= right
        self.parent = parent
        self.height = 1
        self.payload = self.key

class AVL_Tree:
    def __init__(self):
        self.root = None

    def height(self, node: Node) -> int:
        if node == None:
            return 0
        return node.height

    def right_rotate(self, y: Node):
        x = y.left
        y.left = x.right
        if x.right != None:
            x.right.parent = y
        x.parent = y.parent
        if self.root == y:
            self.root = x
        else:
            if y.parent.left == y:
                y.parent.left = x
            else:
                y.parent.right = x
        x.right = y
        y.parent = x

        y.height = max(self.height(y.left), self.height(y.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1

    def left_rotate(self, x: Node):
        y = x.right
        x.right = y.left

        if y.left != None:
           y.left.parent = x
        y.parent = x.parent

        if self.root == x:
            self.root = y
        else:
            if x.parent.left == x:
               x.parent.left = y
            else:
                x.parent.right = y
        y.left = x
        x.parent = y

        x.height = max(self.height(x.left), self.height(x.right)) + 1
        y.height = max(self.height(y.left), self.height(y.right)) + 1

    def get_balance(self, node: Node):
        if node == None:
            return 0

        return self.height(node.left) - self.height(node.right)

    def insert(self, key: int, insertion_point=None):
        node = Node(key)
        # If the tree is empty then assign new node to root
        if self.root == None:
            self.root = Node(key)
            return

        if insertion_point == None:
            insertion_point = self.root

        if key < insertion_point.key:
            if insertion_point.left:
                self.insert(key, insertion_point.left)
            else:
                insertion_point.left = node
                node.parent = insertion_point
        elif key > insertion_point.key:
            if insertion_point.right:
                self.insert(key, insertion_point.right)
            else:
                insertion_point.right = node
                node.parent = insertion_point
        else:
            return

        insertion_point.height = 1 + max(self.height(insertion_point.left), self.height(insertion_point.right))
        balance = self.get_balance(insertion_point)

        if balance > 1 and key < insertion_point.left.key:
            # Left Left
            self.right_rotate(insertion_point)
        elif balance < -1 and key > insertion_point.right.key:
            # Right Right
            self.left_rotate(insertion_point)
        elif balance > 1 and key > insertion_point.left.key:
            # Left Right
            self.left_rotate(insertion_point.left)
            self.right_rotate(insertion_point)
        elif balance < -1 and key < insertion_point.right.key:
            # Right Left
            self.right_rotate(insertion_point.right)
            self.left_rotate(insertion_point)



    def get(self, key: int):
        if self.root:
            res = self._get(key,self.root)
            if res:
                return res
            else:
                return None
        else:
            return None

    def _get(self, key: int, currentNode: Node):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.left)
        else:
            return self._get(key,currentNode.right)

    def __getitem__(self,key: int):
        """ Overloads [] getter to use get() """
        return self.get(key)

    def min_value(self, key: int):
        """ Return the lowest value key in subtree with root 'node' """
        current = self.get(key)
        while current.left != None:
            current = current.left
        return current.key

    def delete(self, key: int, root: Node = None):
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
        if self.root == None:
            return
        if root == None:
            root = self.root

        ## Find node to delete
        # if key < root then recurse left
        if key < root.key:
            self.delete(key, root.left)
        # if key > root then recurse right
        elif key > root.key:
            self.delete(key, root.right)
        # otherwise key == root. Delete root
        else:
            # root is a leaf
            if root.left == None and root.right == None:
                if root == root.parent.left:
                    root.parent.left = None
                else:
                    root.parent.right = None
            # root has both children
            elif root.left != None and root.right != None:
                succ = self.get(self.min_value(root.right.key))
                root.key = succ.key
                root.payload = succ.payload
                # Succ is a leaf 
                # (succ cannot have a left child 
                # because it is the min)
                if succ.right == None:
                    # Succ is a left child
                    if succ.parent.left == succ:
                        succ.parent.left = None
                    # Succ is a right child
                    else:
                        succ.parent.right = None
                # Succ has a right child
                else:
                    # Succ is a left child
                    if succ.parent.left == succ:
                        succ.parent.left = succ.right
                        succ.right.parent = succ.parent
                    # Succ is a right child
                    else:
                        succ.parent.right = succ.right
                        succ.right.parent = succ.parent
            # root has one child
            else:
                # Root is left child:
                if root.parent.left == root:
                    # Child is left
                    if root.left != None:
                        root.left.parent = root.parent
                        root.parent.left = root.left
                    else:
                        root.right.parent = root.parent
                        root.parent.left = root.right
                # Root is right child
                else:
                    # Child is left
                    if root.left != None:
                        root.left.parent = root.parent
                        root.parent.right = root.left
                    else:
                        root.right.parent = root.parent
                        root.parent.right = root.right

        # Update height of node
        root.height = max(self.height(root.left), self.height(root.right)) + 1

        # Get balance factor
        balance = self.get_balance(root)
        # Use balance factor to rotate

        # Left Left
        if balance > 1 and self.get_balance(root.left) >= 0:
            self.right_rotate(root)
        # Left Right
        if balance > 1 and self.get_balance(root.left) < 0:
            self.left_rotate(root.left)
            self.right_rotate(root)
        # Right Right
        if balance < -1 and self.get_balance(root.right) <= 0:
            self.left_rotate(root)
        # Right Left
        if balance < -1 and self.get_balance(root.right) > 0:
            self.right_rotate(root.right)
            self.left_rotate(root)

def traverse(rootnode: Node):
    thislevel = [rootnode]
    while thislevel:
        nextlevel = list()
        row_string = ""
        for n in thislevel:
            if n.parent != None:
                if n.parent.left == n:
                    relation = "L"
                elif n.parent.right == n:
                    relation = "R"
            else:
                relation = "ro"
            row_string += str(n.key) + str((relation, n.height)) + " "
            if n.left: nextlevel.append(n.left)
            if n.right: nextlevel.append(n.right)
        print(row_string)
        thislevel = nextlevel


if __name__ == '__main__':
    tree = AVL_Tree()
    tree.insert(10)
    tree.insert(15)
    tree.insert(11)
    tree.insert(20)
    tree.insert(17)
    tree.insert(25)
    tree.insert(18)
    tree.insert(19)
    tree.delete(20)
    traverse(tree.root)
