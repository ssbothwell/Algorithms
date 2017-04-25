#!/usr/bin/env python
from collections import deque
from itertools import chain, compress

"""
Prims Minimum Spanning Tree Algorithm

# V is the set of all nodes
# X is the set of spanned nodes thus far
X = []
# s is the currently chosen node
s = node
# T is the edges we have commited to as part of the MST
T = []
while X != V:
    1.let e be the cheapest edge of s with its second
        node (v) outside of X
    2.Add e to T and v to X


Running Time:
-O(n) iterations
-O(m) time per iterations
Total: O(m*n)

"""

def prim(graph, nodes):
    s = min(nodes)
    X = set([s])
    V = nodes
    T = set()
    cost = 0
    while X != V:
        e_cost = float('inf')
        for node in X:
            for edge in graph[node]:
                if edge[1] < e_cost and edge[0] not in X:
                    e_cost = edge[1]
                    e = edge[0]
        cost += e_cost
        X.add(e)
        s = e
    return cost

def create_edges(filename):
    """ Generate edge list from text file """
    file = open(filename, 'r')
    # Map each line of test data to a line in the data list:
    data = map(lambda x: x.rstrip().split(' '), file)
    data = map(lambda x: map(int, x), data)
    return data

def generate_graph(edge_list):
    """
    map edge list into a dictionary
    also generate set of all nodes
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
        graph_dict[edge[0]].append((edge[1],edge[2]))
        graph_dict[edge[1]].append((edge[0],edge[2]))
    return graph_dict, node_set

if __name__ == '__main__':
    edges = create_edges('prim_edges.txt')
    graph, node_set = generate_graph(edges)
    print prim(graph, node_set)
