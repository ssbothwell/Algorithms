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
def djikstra(graph, source):
    explored_set = set()
    all_nodes = set(graph.keys())
    node_distances = create_distance_dict(graph)
    node_distances[source] = 0
    while explored_set != all_nodes:
        current_node = min_distance(node_distances, explored_set)
        explored_set.add(current_node)
        update_distances(graph, node_distances, current_node)
    return node_distances

def min_distance(distances_dict, explored_set):
    """ Helper function returns lowest distance node not yet explored """
    minimum = float("infinity")
    for node in distances_dict.keys():
        if node not in explored_set and distances_dict[node] <= minimum:
            minimum, min_index = distances_dict[node], node
    return min_index


def update_distances(graph, distances_dict, current_node):
    """ Helper function updates neighbor's distances """
    for n in graph[current_node]:
        if distances_dict[n[0]] > distances_dict[current_node] + n[1]:
            distances_dict[n[0]] = distances_dict[current_node] + n[1]


#def search(graph, source, nodeDistances):
#    nodeDistances[source] = 0
#    queue = deque([source])
#    while len(queue) != 0:
#        n = queue.popleft()
#        for m in graph[n]:
#        # Iterate each node connected to n
#            if m and nodeDistances[m[0]] > nodeDistances[n] + m[1] :
#            # Compare current m score and update if n + n-m edge is shorter
#                nodeDistances[m[0]] = nodeDistances[n] + m[1]
#                # add m to search queue
#                queue.extend([m[0]])
#
#    return nodeDistances


def create_graph(filename):
    """ Generate edge list from text file """
    file = open(filename, 'r')
    # Map each line of test data to a line in the data list:
    data = map(lambda x: x.rstrip().split('\t'), file)
    # Map data to a dict with index 0 of each line as key and
    # the remaining elemts as a list of tuples
    data = { int(x[0]): [(int(y.split(',')[0]), int(y.split(',')[1])) for y in x[1:]] for x in data}
    return data

def create_distance_dict(graph):
    """ instantiate nodeDistances dict """
    nodeDistances = { x: float("infinity") for x in graph.keys() }
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
    1: [(2,1),(8,2)],
    2: [(1,1),(3,1)],
    3: [(2,1),(4,1)],
    4: [(3,1),(5,1)],
    5: [(4,1),(6,1)],
    6: [(5,1),(7,1)],
    7: [(6,1),(8,1)],
    8: [(7,1),(1,2)],
}

if __name__ == '__main__':
    #graph = create_graph('djikstra_test.txt')
    #nodeDistances = create_distance_dict(graph)
    #print search(graph, 1, nodeDistances)
    print djikstra(graph, 1)
