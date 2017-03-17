#!/usr/bin/env python
import unittest
from dfsComputeStrongComponents import *

class testDfsStrongComponents(unittest.TestCase):
    def setUp(self):
        self.edges_a = createEdgeList('test_data_a.txt')
        self.edges_b = createEdgeList('test_data_b.txt')
        self.edges_c = createEdgeList('test_data_c.txt')
        self.edges_d = createEdgeList('test_data_d.txt')
        self.edges_e = createEdgeList('test_data_e.txt')

    def test_createEdgeList(self):
        self.assertEqual(createEdgeList('test_data_a.txt'), [[1, 4], [2, 8], [3, 6], [4, 7], [5, 2], [6, 9], [7, 1], [8, 5], [8, 6], [9, 7], [9, 3]])

    def test_createGraphDict(self):
        self.assertEqual(createGraphDict(self.edges_e), {1: [2], 2: [3, 4, 5], 3: [6], 4: [5, 7], 5: [2, 6, 7], 6: [3, 8], 7: [8, 10], 8: [7], 9: [7], 10: [9, 11], 11: [12], 12: [10]})

    def test_calculateStrongComponents_a(self):
        self.assertEqual(calculateStrongComponents(createGraphDict(self.edges_a)),
        [3,3,3])

    def test_calculateStrongComponents_b(self):
        self.assertEqual(calculateStrongComponents(createGraphDict(self.edges_b)),
        [3,3,2])

    def test_calculateStrongComponents_c(self):
        self.assertEqual(calculateStrongComponents(createGraphDict(self.edges_c)),
        [3,3,1,1])

    def test_calculateStrongComponents_d(self):
        self.assertEqual(calculateStrongComponents(createGraphDict(self.edges_d)),
        [7,1])

    def test_calculateStrongComponents_e(self):
        self.assertEqual(calculateStrongComponents(createGraphDict(self.edges_e)),
        [6,3,2,1])




if __name__ == '__main__':
    unittest.main()
