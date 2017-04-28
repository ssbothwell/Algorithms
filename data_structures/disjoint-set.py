#!/usr/bin/env python

"""
Disjoint-Set Data Structure

Keeps track of a set of elements partitioned into
disjoint (nonoverlapping) sets. Partition names
(representatives) are chosen arbitrarily from
elements at creation.


Operations:
    -Find: Determin which set the element is in.
    -Union: Join two sets into a single set. The
    new set takes on the representative of the
    larger set.
    -Make_Set: Creates a singleton set partition.

"""

class disjoint_set(object):
    def __init__(self):
        self.partitions_count = 0
        self.size = {}
        self.parent = {}

    def make_set(self, element):
        if self.find(element) == False:
            self.parent[element] = element
            self.size[element] = 1
            self.partitions_count += 1

    def union(self, x, y):
        xParent = self.find(x)
        yParent = self.find(y)
        if xParent != yParent:
            if self.size[xParent] < self.size[yParent]:
                self.parent[xParent] = yParent
                self.size[yParent] += self.size[xParent]
                self.partitions_count -= 1
            else:
                self.parent[yParent] = xParent
                self.size[xParent] += self.size[yParent]
                self.partitions_count -= 1

    def find(self, element):
        if element in self.parent:
            if element == self.parent[element]:
                return element
            root = self.parent[element]
            while self.parent[root] != root:
                root = self.find(self.parent[root])
            self.parent[element] = root
            return root
        return False


if __name__ == '__main__':
    t = disjoint_set()
    t.make_set(1)
    t.make_set(2)
    t.make_set(3)
    t.make_set(4)
    t.make_set(5)
    print("Create 5 singleton partitions")
    print(t.partitions_count)
    print("Union two singletons into a single partition")
    t.union(1,2)
    print("Union three singletones into a single partition")
    t.union(3,4)
    t.union(5,4)
    print("Union a single partition")
    t.union(2,4)
    print("Parent List: %s" % t.parent)
    print("Partition Count: %s" % t.partitions_count)
    print("Parent of element 2: %s" % t.find(2))
    print("Parent List: %s" % t.parent)
