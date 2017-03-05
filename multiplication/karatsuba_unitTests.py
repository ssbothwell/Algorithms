#!/usr/bin/env python
import unittest
from karatsuba import *

class testMultiplicationValues(unittest.TestCase):
    def setUp(self):
        pass

    def test_a(self):
        self.assertEqual(karat(2,2), 4)

    def test_b(self):
        self.assertEqual(karat(2,10), 20)

    def test_c(self):
        self.assertEqual(karat(1234,5678), 7006652)

if __name__ == '__main__':
    unittest.main()
