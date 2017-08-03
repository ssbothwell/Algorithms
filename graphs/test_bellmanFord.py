#!/usr/bin/env python
import unittest
from bellmanFord import *

class testDfsStrongComponents(unittest.TestCase):
    def setUp(self):
        pass

    def test_no_negatives(self):
        vertices = ['s', 'v', 'x', 'w', 't']
        edges = [('s', 'v', 2)
                ,('s', 'x', 4)
                ,('v', 'x', 1)
                ,('v', 'w', 2)
                ,('x', 't', 4)
                ,('w', 't', 2)
                ]

        self.assertEqual(bellmanFord(vertices, edges, 's'), {'s': 0, 'v': 2, 'x': 3, 'w': 4, 't': 6})

    def test_negatives(self):
        vertices = ['s', 'a', 'b', 'c', 'd', 'e']
        edges = [('s', 'a', 10)
                ,('s', 'e', 8)
                ,('e', 'd', 1)
                ,('d', 'a', -4)
                ,('d', 'c', -1)
                ,('c', 'b', -2)
                ,('b', 'a', 1)
                ,('a', 'c', 2)
                ]

        self.assertEqual(bellmanFord(vertices, edges, 's'), {'s': 0, 'a': 5, 'b': 5, 'c': 7, 'd': 9, 'e': 8})




if __name__ == '__main__':
    unittest.main()

