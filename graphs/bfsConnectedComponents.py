#!/usr/bin/env python
from collections import deque

def bfSearch(gDict, startingNode, exploredDict=None):
    if exploredDict == None:
        exploredDict = { key: (True if key == startingNode else False)  for key in gDict }
    else:
        exploredDict[startingNode] = True

    distDict = {startingNode: 0}
    queue = deque([startingNode])

    while len(queue) != 0:
        n = queue.popleft()
        for m in graphDict[n]:
            if exploredDict[m] == False:
                distDict[m] = distDict[n] + 1
                exploredDict[m] = True
                queue.extend(m)
    return [ key for key in distDict ]

def connectedComponents(gDict):
    exploredDict = { key: False for key in gDict }
    connectedDict = []
    for n in gDict:
        if exploredDict[n] == False:
            connectedDict.append(bfSearch(gDict, n, exploredDict))
    return connectedDict

graphDict = {
    '1': ['3','5'],
    '2': ['4'],
    '3': ['1','5'],
    '4': ['2'],
    '5': ['1','3', '7', '9'],
    '6': ['8','10'],
    '7': ['5'],
    '8': ['6','10'],
    '9': ['5'],
    '10': ['6','8']
}

print connectedComponents(graphDict)
