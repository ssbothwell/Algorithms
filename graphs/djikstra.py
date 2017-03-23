#!/usr/bin/env python
from collections import deque

"""
Dijkstra's Shorted Path Algorithm

1. Assign every node an initial value (zero for source, infinity for everything else).

2. Create a set for visited and unvisited nodes. Add source to visited set.

3. Use breadth first search to check all nodes adjacent to the source.
Compare current node values to source node + source -> new node edge. Assign
the node the smaller value.

4. Mark the current node as visited and remove it from the unvisited set.

5. Stop if the destination node has been marked visited or when the remaining
unvited nodes are marked infinity.

6. Otherwise select the unvisited node with the smallest assigned distance
and as source and repeat from step 3.
"""

def search(graph, source, nodeDistances):
    queue = deque([source])
    while len(queue) != 0:
        n = queue.popleft()
        for m in graph[n]:
        # Iterate each node connected to n
            if m and nodeDistances[m[0]] > nodeDistances[n] + m[1] :
            # Compare current m score and update if n + n-m edge is shorter
                nodeDistances[m[0]] = nodeDistances[n] + m[1]
                # add m to search queue
                queue.extend([m[0]])

    return nodeDistances


nodeDistances = {
    1: 0,
    2: float("infinity"),
    3: float("infinity"),
    4: float("infinity"),
    5: float("infinity"),
    6: float("infinity"),
    7: float("infinity"),
    8: float("infinity"),
    }
graph = {
    1: [[2,1],[8,2]],
    2: [[1,1],[3,1]],
    3: [[2,1],[4,1]],
    4: [[3,1],[5,1]],
    5: [[4,1],[6,1]],
    6: [[5,1],[7,1]],
    7: [[6,1],[8,1]],
    8: [[7,1],[1,2]],
}
if __name__ == '__main__':
    print search(graph, 1, nodeDistances)
