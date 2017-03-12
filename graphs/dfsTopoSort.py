#!/usr/bin/env python

def dfSearch(gDict, startingNode, exploredDict, sortList):
    exploredDict[startingNode] = True
    for n in gDict[startingNode]:
        if exploredDict[n] == False:
            dfSearch(gDict, n, exploredDict, sortList)
    sortList.append(startingNode)

def dfsLoop(gDict):
    exploredDict = { key: False for key in gDict.keys() }
    sortList = []

    for n in gDict:
        if exploredDict[n] == False:
            dfSearch(gDict, n, exploredDict, sortList)

    return sortList


graphDict = {
    'a': ['b','c'],
    'b': ['d'],
    'c': ['d'],
    'd': [],
}

print dfsLoop(graphDict)
