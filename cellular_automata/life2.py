#!/usr/bin/env python
from itertools import chain

"""
Conways Game of Life

From Jack Diederich's Presentation "Stop Writing Classes"
https://www.youtube.com/watch?v=o9pEzgHorH0

"""

def neighbors(point):
    x, y = point
    yield x + 1, y
    yield x - 1, y
    yield x, y + 1
    yield x, y - 1
    yield x + 1, y + 1
    yield x + 1, y - 1
    yield x - 1, y - 1
    yield x - 1, y + 1

def advance(board):
    newstate = set()
    # - map(neighbors, board) calls neighbors on each position
    # in board, creating a generator for each position in board. 
    # - chain(*map(...) combines these into one iterator which is
    # then passed into a set. 
    # - The set is then bitwise OR'd with board. Not sure why..
    recalc = board | set(chain(*map(neighbors, board)))
    # Iterate through points in recalc
    for point in recalc:
        # sum of all neighbors of point that are in board
        count = sum((neigh in board)
                    for neigh in neighbors(point))
        # Add point to newstate if 3 neighbors or point and 2
        # neighbors are in board
        if count == 3 or (count == 2 and point in board):
            newstate.add(point)
    return newstate

if __name__ == '__main__':
    glider = set([(0,0), (1,0), (2,0), (0,1), (1,2)])
    for i in range(10):
        glider = advance(glider)
    print(glider)
