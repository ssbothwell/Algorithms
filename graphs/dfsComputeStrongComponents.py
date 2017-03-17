#!/usr/bin/env python
# Kosaraju's Two Pass Algorithm

def reverseGraph(graph):
    """ Reverse the key/value pairs in linked list graph """
    rGraph = { el: [] for el in range(1, 1+max(max(graph.keys()),max(graph.values()[0])))}
    for key in graph:
        for val in graph[key]:
            if val in rGraph:
                rGraph[val].append(key)
            else:
                rGraph[val] = [key]
    return rGraph


def visit(gDict, startingNode, exploredDict, t):
    """ Visit each node using DFS generate finishing time list """

    exploredDict[startingNode] = True
    for n in gDict[startingNode]:
        if exploredDict[n] == False:
            visit(gDict, n, exploredDict, t)
    t.append(startingNode)


def assign(gdict, startingnode, exploredDict, leader, sComponent):
    """ Second pass DFS group nodes with leaders """

    exploredDict[startingnode] = True
    for n in gdict[startingnode]:
        if exploredDict[n] == False:
            sComponent.append(n)
            assign(gdict, n, exploredDict, leader, sComponent)


def dfsloop(gDict):
    # Pass Two Order
    t = []
    # Current `leader` Vertex
    s = -1
    strongComponents = []
    exploredDict = { key: False for key in gDict.keys() }
    # First Pass
    for i in reversed(gDict.keys()):
        if exploredDict[i] == False:
            s = i
            visit(gDict, i, exploredDict, t)

    # Second Pass
    rGraph = reverseGraph(gDict)
    exploredDict = { key: False for key in rGraph.keys() }
    #t = filter(lambda x: x != 5, t)
    # Uses finishing times as order
    for i in reversed(t):
        s = i
        if exploredDict[i] == False:
            sComponent = [s]
            assign(rGraph, i, exploredDict, s, sComponent)
            strongComponents.append(sComponent)
    return strongComponents


graph = {
    1: [7],
    2: [5],
    3: [9],
    4: [1],
    5: [8],
    6: [3,8],
    7: [4,9],
    8: [2],
    9: [6]
}

# Load data and process into a graph dict
file = open('scc2.txt', 'r')
data = map(lambda x: [int(x[0]), int(x[1])], map(lambda x: x.rstrip().split(' '), file))

file = open('scc2.txt', 'r')
rData = map(lambda x: [int(x[1]), int(x[0])], map(lambda x: x.rstrip().split(' '), file))

#graphDict = { el[0]: [] for el in data}
graphDict = { el: [] for el in range(1, 1+max(map(lambda x: max(x), data)))}
#rGraphDict = { el: [] for el in range(1, 1+max(map(lambda x: max(x), rData)))}
map(lambda el: graphDict[el[0]].append(el[1]), data)
#map(lambda el: rGraphDict[el[0]].append(el[1]), rData)
print sorted(map(lambda x: len(x), dfsloop(graphDict)), reverse=True)

