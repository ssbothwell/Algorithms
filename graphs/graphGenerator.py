#!/usr/bin/env python
# Generate an edgelist for a directed graph of arbitrary size

import os,sys,random

def generateNodes(size):
    nodes = []
    for i in range(1,size+1):
        nodes.append(i)

    return nodes


def generateEdges(nodes, edgeCount):
    edgeList = []

    for _ in range(0,edgeCount):
        edge = random.sample(range(1, len(nodes)), 2)
        print "%s %s" % (edge[0], edge[1])


if __name__ == '__main__':
    generateEdges(generateNodes(10), 10000)
