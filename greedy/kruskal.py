#!/usr/bin/env python
from collections import deque
from itertools import chain, compress
from operator import itemgetter

"""
Kruskal's MST algorithm

Pseudocode:
Sort edges in order of increasing cost.
T = 0 <-- spanning tree in progress
for each edge:
    if T + edge has no cycles:
        T.append(edge)
return T

Proof:
Let T* = output of Kruskal's algorithm on input graph G
1. T* has no cycles (kruskal's excludes edges which create cycles)
2. T* is connected and thus a spanning tree
    Empty Cut Lemma: Graph is connected IFF if for each possible
      cut it has one edge crossing that cut.
        -Because graph G is connected, for a given cut (a,b), G has
        a crossing edge.
        -Kruskal will always include the first edge crossing (a,b)
        because kruskal considers all edges, will only exclude
        an edge if it creates a cycle, and a cycle is only created
        when more then one edge cross a cut.
3. Every edge of T* is justified by the cut property (implying MST).
    -Consider the iteration where edge (u,v) has been added to T*:
        Since T+(u,v) has no cycles, T has no (u,v) path.
        Since Kruskal picks the first edge cross a cut and edges
        were sorted cheapest to most expensive, the edge (u,v) must
        be the cheapest edge crossing the cut.

"""

def kruskal(edgeList):
    T = disjoint_set()
    sortedEdges = sort_edges(edgeList)
    T.make_set(sortedEdges[0])
    for edge in sortedEdges:
        
    return T.forest

def sort_edges(edgeList):
    """
    Sorts edgeList by weight ascending
    Input: edgeList <- [(edge),(edge)] <- [(node,node,weight)]
    Output: edgeListSorted
    """
    return sorted(edgeList, key=itemgetter(2))

def create_edges(filename):
    """ Generate edge list from text file """
    file = open(filename, 'r')
    # Map each line of test data to a line in the data list:
    data = map(lambda x: x.rstrip().split(' '), file)
    data = map(lambda x: map(int, x), data)
    return data

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
    edgeList = [(1,2,1),(2,3,7),(1,3,5),(3,4,6),(1,4,3),(5,4,2),(1,5,4)]
    print(kruskal(edgeList))
