#!/usr/bin/env python
import unittest
from insertion_sort import *

class testInsertionSort(unittest.TestCase):
    def setUp(self):
        pass

    def test_a(self):
        self.assertEqual(insertion_sort([5,4,3,2,1]), [1,2,3,4,5])

    def test_b(self):
        self.assertEqual(insertion_sort([1,2,3,4,5]), [1,2,3,4,5])

    def test_c(self):
        self.assertEqual(insertion_sort([10,8,6,4,2,0]), [0,2,4,6,8,10])


if __name__ == '__main__':
    unittest.main()
