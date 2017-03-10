#!/usr/bin/env python
import random
import copy

def pick(g):
    v = random.sample(g.keys(),1)[0]
    e = random.sample(g[v],1)[0]
    return v,e


def cleanGraph(g):
    for v in g:
        g[v] = filter(lambda x: x != v, g[v])
    return g

def checkMin(g):
    while len(g.keys()) > 2:
        v,e = pick(g)
        g[v] = g[v] + g[e]
        del g[e]

        for vertex in g:
            g[vertex] = map(lambda x: v if x == e else x, g[vertex])

        cleanGraph(g)
    return len(g[g.keys()[0]])

file = open('karger.txt', 'r')
raw_data = [ [ int(el) for el in line.strip().split("\t") ] for line in file ]

def outer():
    graph = { line[0]: [line[i] for i in range(1,len(line))] for line in raw_data }
    return checkMin(graph)


print min([ outer() for _ in range(0,100) ])
