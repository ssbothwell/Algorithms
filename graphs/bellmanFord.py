#!/usr/bin/env python
from collections import deque
from typing import List, Tuple
import sys

def bellmanFord(nodes: List[str], edges: List[tuple], source: str) -> tuple:

    # Initialize Arrays
    distance = {n: (sys.maxsize if n != source else 0) for n in nodes}
    predecessor = {n: None for n in nodes}

    # Relax edges
    for i in range(len(nodes)-1):
        terminator = True
        for u, v, w in edges:
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                predecessor[v] = u
                terminator = False
        if terminator == True:
            break

    # Check for negative weight cycles
    for u, v, w in edges:
        if distance[u] + w < distance[v]:
            print("Graph contains a negative weight cycle")

    return distance


if __name__ == '__main__':
    vertices = ['s', 'v', 'x', 'w', 't']
    edges = [('s', 'v', 2)
            ,('s', 'x', 4)
            ,('v', 'x', 1)
            ,('v', 'w', 2)
            ,('x', 't', 4)
            ,('w', 't', 2)
            ]
    print(bellmanFord(vertices, edges, 's'))
