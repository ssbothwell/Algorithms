#!/usr/bin/env python
from operator import itemgetter

"""
MST Clustering Algorithm

Given a set of nodes in space and a specified number of clusters,
group the nodes into clusters by shortest distances.


Pseudocode:
K = Cluster Count Target
X = sorted edge list
D = disjoint-set
for each edge in X:
    if edge nodes are in seperate sets:
        union those sets
    if D.size = K:
        break
return T
"""

def k_cluster(edgeLast, K):
    sortedEdges = sort_edges(edgeList)
    D = disjoint_set()
    Max_Distance = 0
    for edge in sortedEdges:
        D.make_set(edge[0])
        D.make_set(edge[1])
    for edge in sortedEdges:
        x = D.find(edge[0])
        y = D.find(edge[1])
        if x != y:
            if D.partitions_count == K:
                return D.parent, D.partitions_count
            D.union(x,y)
    return D.partitions_count

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
    data = [ [int(y) for y in x.rstrip().split(' ')] for x in file]
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
    edgeList = [(1,2,1  )
               ,(1,3,100)
               ,(1,4,100)
               ,(1,5,100)
               ,(2,3,100)
               ,(2,4,100)
               ,(2,5,100)
               ,(3,4,10 )
               ,(3,5,10 )
               ,(4,5,10 )
               ]
    edgeList = create_edges('data_clustering.txt')
    #edgeList =  [(1,2,1)
    #            ,(1,5,6)
    #            ,(2,3,3)
    #            ,(2,6,6)
    #            ,(3,4,5)
    #            ,(4,5,4)
    #            ,(5,6,2)
    #            ]
    print(k_cluster(edgeList, 4))
