#!/usr/bin/env python

def dfSearch(gDict, startingNode, exploredDict=None):
    if exploredDict == None:
        exploredDict = { key: False for key in gDict.keys() }
    exploredDict[startingNode] = True
    for n in gDict[startingNode]:
        if exploredDict[n] == False:
            dfSearch(gDict, n, exploredDict)
    return exploredDict

graphDict = {
    's': ['a','b'],
    'a': ['s','c'],
    'b': ['s','c', 'd'],
    'c': ['a','b','d','o'],
    'd': ['b','c','o'],
    'o': ['c','d']
}

print dfSearch(graphDict, 's')
