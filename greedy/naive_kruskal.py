#!/usr/bin/env python
from collections import deque
from itertools import chain, compress
from operator import itemgetter

"""
Niave Kruskal's MST algorithm

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
    T = []
    sortedEdges = sort_edges(edgeList)
    T.append(sortedEdges[0])
    for edge in sortedEdges:
        if check_cycles(T, edge) == False:
            T.append(edge)
    return T

def sort_edges(edgeList):
    """
    Sorts edgeList by weight ascending
    Input: edgeList <- [(edge),(edge)] <- [(node,node,weight)]
    Output: edgeListSorted
    """
    return sorted(edgeList, key=itemgetter(2))

def check_cycles(edges, newEdge):
    """
    Executes breadth first search on the edge list check
    if there is already a connection between the nodes of
    newEdge. If there is a connection then adding newEdge
    to the spanning tree would create a cycle.
    Output:
        True == A cycle would be created
        False == A cycle would not be created
    """
    graph = createGraphDict(edges)
    if newEdge[0] in graph:
        searchResult = bfSearch(graph, newEdge[0])
        if newEdge[1] in searchResult:
            return True
    elif newEdge[1] in graph:
        searchResult = bfSearch(graph, newEdge[1])
        if newEdge[0] in searchResult:
            return True
    return False


def createGraphDict(edge_list):
    """
    map edge list into a dictionary
    """
    # strip weight from list
    data = map(lambda x: list(x[:2]), edge_list)
    # flatten list to get list of all nodes
    data = list(chain.from_iterable(data))
    # Load into a set to elminate repeats
    node_set = set(data)
    # Load set into graph dict
    graph_dict = { x:[] for x in node_set }

    # Load edge data into graph dict 
    for edge in edge_list:
        graph_dict[edge[0]].append(edge[1])
        graph_dict[edge[1]].append(edge[0])
    return graph_dict

def bfSearch(gDict, startingNode):
    exploredDict = { key: (True if key == startingNode else False)  for key in gDict.keys() }
    distDict = {startingNode: 0}
    queue = deque(str(startingNode))

    while len(queue) != 0:
        n = int(queue.popleft())
        for m in gDict[n]:
            if exploredDict[m] == False:
                distDict[m] = distDict[n] + 1
                exploredDict[m] = True
                queue.extend(str(m))

    return distDict

def create_edges(filename):
    """ Generate edge list from text file """
    file = open(filename, 'r')
    # Map each line of test data to a line in the data list:
    data = map(lambda x: x.rstrip().split(' '), file)
    data = map(lambda x: map(int, x), data)
    return data

if __name__ == '__main__':
    edgeList = [(1,2,1),(2,3,7),(1,3,5),(3,4,6),(1,4,3),(5,4,2),(1,5,4)]
    print(kruskal(edgeList))
