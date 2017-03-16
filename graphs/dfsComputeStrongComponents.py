#!/usr/bin/env python
# Kosaraju's Two Pass Algorithm

def reverseGraph(graph):
    """ Reverse the key/value pairs in linked list graph """
    rGraph = {}
    for key in graph:
        for val in graph[key]:
            if val in rGraph:
                rGraph[val].append(key)
            else:
                rGraph[val] = [key]
    return rGraph


def visit(gDict, startingNode, t):
    """ Visit each node using DFS generate finishing time list """
    global exploredDict

    exploredDict[startingNode] = True
    for n in gDict[startingNode]:
        if exploredDict[n] == False:
            visit(gDict, n, t)
    t.append(startingNode)


def assign(gdict, startingnode, leader):
    """ Second pass DFS group nodes with leaders """
    global exploredDict
    global strongComponents

    exploredDict[startingnode] = True
    for n in gdict[startingnode]:
        if exploredDict[n] == False:
            strongComponents[leader].append(n)
            assign(gdict, n, leader)


def dfsloop(gDict):
    global exploredDict
    global strongComponents
    # Pass Two Order
    t = []
    # Current `leader` Vertex
    s = -1
    strongComponents = {}
    exploredDict = { key: False for key in gDict.keys() }

    # First Pass
    for i in range(len(gDict), 0, -1):
        if exploredDict[i] == False:
            s = i
            visit(gDict, i, t)

    # Second Pass
    rGraph = reverseGraph(graph)
    exploredDict = { key: False for key in gDict.keys() }
    # Uses finishing times as order
    for i in range(len(t)-1, -1, -1):
        s = t[i]
        if exploredDict[t[i]] == False:
            strongComponents[s] = []
            assign(rGraph, t[i], s)
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

print dfsloop(graph)

