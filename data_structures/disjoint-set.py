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

class partition(object):
    def __init__(self, element=None):
        self.size = 0
        if element == None:
            self.contents = set()
            self.representative = None
        else:
            self.contents = {element}
            self.representative = element
            self.size = 1

    def find(self, element):
        return element in self.contents

    def add(self, partition):
        self.contents = self.contents.union(partition)
        self.size = len(self.contents)

    def show(self):
        return self.contents

    def __repr__(self):
        return str(self.contents)

class disjoint_set(object):
    def __init__(self):
        self.partitions_count = 0
        self.forest = {}

    def make_set(self, element):
        new_partition = partition(element)
        self.forest[new_partition.representative] = new_partition
        self.partitions_count += 1

    def union(self, x, y):
        if x != y:
            if self.forest[x].size < self.forest[y].size:
                self.forest[y].add(self.forest[x].show())
                self.delete(x)
            else:
                self.forest[x].add(self.forest[y].show())
                self.delete(y)
            self.partitions_count -= 1

    def find(self, element):
        for partition in self.forest.keys():
            if self.forest[partition].find(element):
                return self.forest[partition].representative
        return False

    def delete(self, partition):
        del self.forest[partition]

if __name__ == '__main__':
    t = disjoint_set()
    t.make_set(1)
    t.make_set(2)
    t.make_set(3)
    print("Create 3 singleton partitions:")
    print(t.forest)
    print("Union two into a single partition:")
    t.union(1,2)
    print(t.forest)
    print("Union partitions 1 and 3")
    t.union(3,1)
    print(t.forest)
