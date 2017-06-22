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
    def __init__(self, key, left=None, right=None, parent=None, payload=None):
        self.key = key
        self.left = left
        self.right= right
        self.parent = parent
        self.height = 1
        if payload:
            self.payload = payload
        else:
            self.payload = self.key
        self.count = 1

    #def __iter__(self):
    #    if self.left:
    #        yield from self.left
    #    yield self
    #    if self.right:
    #        yield from self.right
        #if self:
        #    print('foo')
        #    if self.left != None:
        #        for elem in self.left:
        #            yield elem
        #    yield self.key
        #    if self.right != None:
        #        for elem in self.right:
        #            yield elem

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

    def insert(self, key: int, insertion_point=None, payload=None):
        node = Node(key)
        if payload != None:
            node.payload = payload
        # If the tree is empty then assign new node to root
        if self.root == None:
            self.root = node
            return

        if insertion_point == None:
            insertion_point = self.root

        if key == insertion_point.key:
            insertion_point.count += 1
        elif key < insertion_point.key:
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

    def __contains__(self,key):
        if self.get(key):
            return True
        else:
            return False

    def min_value(self, key: int):
        """ Return the lowest value key in subtree with root 'node' """
        current = self.get(key)
        while current.left != None:
            current = current.left
        return current.key

    def delete(self, key: int, starting_node: Node = None):
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
        if starting_node == None:
            starting_node = self.root

        ## Find node to delete
        # if key < starting_node then recurse left
        if key < starting_node.key:
            self.delete(key, starting_node.left)
        # if key > starting_node then recurse right
        elif key > starting_node.key:
            self.delete(key, starting_node.right)
        # otherwise key == starting_node then delete starting_node
        else:
            #if root == self.root:
            #    self.root = None
            #    return
            # Node is a duplicate
            if starting_node.count > 1:
                starting_node.count -= 1
            # Node is a leaf
            elif starting_node.left == None and starting_node.right == None:
                if starting_node == starting_node.parent.left:
                    starting_node.parent.left = None
                else:
                    starting_node.parent.right = None
            # Node has both children
            elif starting_node.left != None and starting_node.right != None:
                succ = self.get(self.min_value(starting_node.right.key))
                starting_node.key = succ.key
                starting_node.payload = succ.payload
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
            # Node has one child
            else:
                if starting_node == self.root:
                    # Child is left
                    if starting_node.left != None:
                        starting_node.left.parent = None
                        self.root = starting_node.left
                    # Child is right
                    else:
                        starting_node.right.parent = None
                        self.root = starting_node.right
                # Node is left child:
                elif starting_node.parent.left == root:
                    # Child is left
                    if starting_node.left != None:
                        starting_node.left.parent = starting_node.parent
                        starting_node.parent.left = starting_node.left
                    # Child is right
                    else:
                        starting_node.right.parent = starting_node.parent
                        starting_node.parent.left = starting_node.right
                # Node is right child
                else:
                    # Child is left
                    if starting_node.left != None:
                        starting_node.left.parent = starting_node.parent
                        starting_node.parent.right = starting_node.left
                    else:
                        starting_node.right.parent = starting_node.parent
                        starting_node.parent.right = starting_node.right

        # Update height of node
        starting_node.height = max(self.height(starting_node.left), self.height(starting_node.right)) + 1

        # Get balance factor
        balance = self.get_balance(starting_node)
        # Use balance factor to rotate

        # Left Left
        if balance > 1 and self.get_balance(starting_node.left) >= 0:
            self.right_rotate(starting_node)
        # Left Right
        if balance > 1 and self.get_balance(starting_node.left) < 0:
            self.left_rotate(starting_node.left)
            self.right_rotate(starting_node)
        # Right Right
        if balance < -1 and self.get_balance(starting_node.right) <= 0:
            self.left_rotate(starting_node)
        # Right Left
        if balance < -1 and self.get_balance(starting_node.right) > 0:
            self.right_rotate(starting_node.right)
            self.left_rotate(starting_node)

    def __delitem__(self,key):
        self.delete(key)

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
    tree.insert(10, payload=5)
    #tree.insert(15)
    #tree.insert(11)
    #tree.insert(20)
    #tree.insert(17)
    tree.insert(25)
    #tree.insert(18)
    tree.delete(10)
    traverse(tree.root)
