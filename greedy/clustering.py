#!/usr/bin/env python

"""
MST Clustering Algorithm

Given a set of nodes in space and a specified number of clusters,
group the nodes into clusters by shortest distances.


Pseudocode:
Sort edges in order of increasing weight (distance).
T = 0 <-- Clustered Nodes
for each edge:
    if T + edge has no cycles:
        T.append(edge)
return T

