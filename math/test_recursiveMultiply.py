#!/usr/bin/env python
import unittest
from recursiveMultiply import *

class testMultiplicationValues(unittest.TestCase):
    def setUp(self):
        pass

    def test_a(self):
        self.assertEqual(rMulti(2,2), 4)

    def test_b(self):
        self.assertEqual(rMulti(2,10), 20)

    def test_c(self):
        self.assertEqual(rMulti(123,567), 69741)

    def test_d(self):
        self.assertEqual(rMulti(-123,567), -69741)

if __name__ == '__main__':
    unittest.main()
