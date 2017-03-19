#!/usr/bin/env python
# Kosaraju's Two Pass Algorithm
# Iterative Version
import random
import time

def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print '%r %2.2f sec' % \
              (method.__name__, te-ts)
        return result

    return timed

def createEdgeList(filename):
    """ Generate edge list from text file """
    file = open(filename, 'r')
    return  map(lambda x: [int(x[0]), int(x[1])], map(lambda x: x.rstrip().split(' '), file))


def createGraphDict(edgeList):
    """ Generate linked list graph from edge list """
    graphDict = { el: [] for el in range(1, 1+max(map(lambda x: max(x), edgeList)))}
    map(lambda el: graphDict[el[0]].append(el[1]), edgeList)

    return graphDict


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


def calculateStrongComponents(graph):
    """ returns a sorted list of strong component sizes """
    return sorted(map(lambda x: len(x), dfsloop(graph)), reverse=True)

def visit(gDict, startingNode, explored, t):
    """ Visit each node using DFS generate finishing time list """
    orderedNodes = set()
    stack = [startingNode]
    while len(stack) != 0:
        n = stack.pop()
        if n not in explored:
            stack.append(n)
            explored.add(n)
            for m in gDict[n]:
                if m not in explored:
                    stack.append(m)
        else:
            if n not in orderedNodes:
                t.append(n)
                orderedNodes.add(n)

def assign(gDict, startingNode, explored, leader, sComponent):
    stack = [startingNode]
    while len(stack) != 0:
        n = stack.pop()
        if n not in explored:
            sComponent.append(n)
            explored.add(n)
            for m in gDict[n]:
                if m not in explored:
                    stack.append(m)


def dfsloop(gDict):
    # Pass Two Order
    t = []
    # Current `leader` Vertex
    s = -1
    strongComponents = []
    explored = set()
    # First Pass
    for i in reversed(sorted(gDict.keys())):
        if i not in explored:
            s = i
            visit(gDict, i, explored, t)

    # Second Pass
    rGraph = reverseGraph(gDict)
    explored = set()
    # Uses finishing times as order
    for i in reversed(t):
        s = i
        if i not in explored:
            sComponent = []
            assign(rGraph, i, explored, s, sComponent)
            strongComponents.append(sComponent)
    return strongComponents

@timeit
def time_wrapper():
    print calculateStrongComponents(createGraphDict(edgeList))[:5]

if __name__ == '__main__':
    edgeList = createEdgeList('scc.txt')
    time_wrapper()
