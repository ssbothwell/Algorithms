#!/usr/bin/env python
from collections import deque

def bfSearch(gDict, startingNode):
    exploredDict = { key: (True if key == startingNode else False)  for key in gDict.keys() }
    distDict = {startingNode: 0}
    queue = deque(startingNode)

    while len(queue) != 0:
        n = queue.popleft()
        for m in graphDict[n]:
            if exploredDict[m] == False:
                distDict[m] = distDict[n] + 1
                exploredDict[m] = True
                queue.extend(m)

    return distDict

graphDict = {
    's': ['a','b'],
    'a': ['s','c'],
    'b': ['s','c', 'd'],
    'c': ['a','b','d','o'],
    'd': ['b','c','o'],
    'o': ['c','d']
}

print(bfSearch(graphDict, 's'))
