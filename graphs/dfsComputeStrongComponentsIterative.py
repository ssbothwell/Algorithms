#!/usr/bin/env python
# Kosaraju's Two Pass Algorithm
# Iterative Version


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


def visit(gDict, startingNode, exploredDict, t):
    """ Visit each node using DFS generate finishing time list """
    stack = [startingNode]
    while len(stack) != 0:
        n = stack.pop()
        if exploredDict[n] == False:
            stack = stack +[n]
            exploredDict[n] = True
            for m in gDict[n]:
                if exploredDict[m] == False:
                    stack.append(m)
        else:
            if exploredDict[n] == True:
                t.append(n)


def assign(gDict, startingNode, exploredDict, leader, sComponent):
    stack = [startingNode]
    while len(stack) != 0:
        n = stack.pop()
        if exploredDict[n] == False:
            sComponent.append(n)
            exploredDict[n] = True
            for m in gDict[n]:
                if exploredDict[m] == False:
                    stack.append(m)


#def assign(gdict, startingnode, exploredDict, leader, sComponent):
#    """ Second pass DFS group nodes with leaders """
#
#    exploredDict[startingnode] = True
#    for n in gdict[startingnode]:
#        if exploredDict[n] == False:
#            sComponent.append(n)
#            assign(gdict, n, exploredDict, leader, sComponent)


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
    # Uses finishing times as order
    for i in reversed(t):
        s = i
        if exploredDict[i] == False:
            sComponent = []
            assign(rGraph, i, exploredDict, s, sComponent)
            strongComponents.append(sComponent)
    return strongComponents



if __name__ == '__main__':
    edgeList = createEdgeList('test_data_a.txt')
    print calculateStrongComponents(createGraphDict(edgeList))
