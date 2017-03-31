#!/usr/bin/env python
import unittest
from median_maintainence import *

class test_median_maintainence(unittest.TestCase):
    def setUp(self):
        pass

    def test_a(self):
        self.assertEqual(median_maintainence([1,666,10,667,100,2,3]), 142)

    def test_b(self):
        self.assertEqual(median_maintainence([6331,2793,1640,9290,225,625,6195,2303,5685,1354]), 9335)


if __name__ == '__main__':
    unittest.main()
