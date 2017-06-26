#!/usr/bin/env python
import unittest
from quicksort_lomuto_median import quick_sort_outer

class testQuickSortLomutoMedian(unittest.TestCase):
    def setUp(self):
        pass

    def test_a(self):
        self.assertEqual(quick_sort_outer([5,4,3,2,1]), [1,2,3,4,5])

    def test_b(self):
        self.assertEqual(quick_sort_outer([1,2,3,4,5]), [1,2,3,4,5])

    def test_c(self):
        self.assertEqual(quick_sort_outer([10,8,6,4,2,0]), [0,2,4,6,8,10])


if __name__ == '__main__':
    unittest.main()
