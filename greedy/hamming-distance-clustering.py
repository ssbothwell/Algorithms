#!/usr/bin/env python
from itertools import product
import time
def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print('%r (%r, %r) %2.2f sec' % \
              (method.__name__, args, kw, te-ts))
        return result

    return timed
"""
MST Clustering Algorithm

A modified version of the Kruskal's Algorithm for calculating
clusters of nodes given as 24bit labels denoting the node's
Hamming distances (the number of differing bits). The hamming 
distance denotes the distance between two nodes.

For example, the nodes:
0 1 1 0 0 1 1 0 0 1 0 1 1 1 1 1 1 0 1 0 1 1 0 1
0 1 0 0 0 1 0 0 0 1 0 1 1 1 1 1 1 0 1 0 0 1 0 1
Have a distance of 3.

Given a set of nodes in space and a specified number of clusters,
group the nodes into clusters by shortest distances.


Pseudocode:
nodeList = hashtable of nodes { 24bit key: integer id}
D = disjoint-set of all nodes
for each Node in nodeList:
    if 24bit codes of hamming distance < 3 are in nodeList:
        union those nodes with Node
return D.setCount
"""
@timeit
def k_cluster(nodeList):
    D = disjoint_set()

    for node in nodeList:
        D.make_set(nodeList[node])
    for node in nodeList:
        for permutation in find_distance_1(node):
            if permutation in nodeList:
                D.union(nodeList[node], nodeList[permutation])
        for permutation in find_distance_2(node):
            if permutation in nodeList:
                D.union(nodeList[node], nodeList[permutation])
    return D.partitions_count

def find_distance_1(node):
    for i, bit in enumerate(node):
        arr = bytearray(node, 'utf8')
        arr[i] = 48 if bit == '1' else 49
        yield arr.decode()

def find_distance_2(value):
    for x, y in product(range(len(value) - 1), range(1, len(value))):
        l = bytearray(value, 'utf8')
        l[x] = 48 if l[x] == 49 else 49  # 48 is ord('0'), 49 is ord('1')
        l[y] = 48 if l[y] == 49 else 49  # 48 is ord('0'), 49 is ord('1')
        yield l.decode()

def create_nodes(filename):
    """ Generate edge list from text file """
    file = open(filename, 'r')
    # Map each line of test data to a line in the data list:
    data = { x.strip().replace(" ", ""): i  for i, x in enumerate(file)}
    return data

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
    #nodes = create_nodes('data_clustering_big.txt')
    nodes = create_nodes('data_hamming.txt')
    print(k_cluster(nodes))
