#!/usr/bin/env python
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

In this optimized version, the disjoint-set data structure is used
to make cycle checks. Worse case running time is O(mlog(n)).

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
    sortedEdges = sort_edges(edgeList)
    T = set()
    D = disjoint_set()
    for edge in sortedEdges:
        D.make_set(edge[0])
        D.make_set(edge[1])
    for edge in sortedEdges:
        x = D.find(edge[0])
        y = D.find(edge[1])
        if x != y:
            T.add(edge)
            D.union(x,y)
    return T

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
    edgeList = [(1,2,1),(2,3,7),(1,3,5),(3,4,6),(1,4,3),(5,4,2),(1,5,4)]
    print(kruskal(edgeList))
