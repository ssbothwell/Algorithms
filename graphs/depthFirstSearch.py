#!/usr/bin/env python

def dfSearch(gDict, startingNode):
    exploredDict = { key: False for key in gDict.keys() }
    stack = [startingNode]
    while len(stack) != 0:
        n = stack.pop()
        if exploredDict[n] == False:
            exploredDict[n] = True
            for m in gDict[n]:
                stack.append(m)

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
