#!/usr/bin/env python
import unittest
from nonRecursiveKaratsuba import *

class testMultiplicationValues(unittest.TestCase):
    def setUp(self):
        pass

    def test_a(self):
        self.assertEqual(karat(2,2), 4)

    def test_b(self):
        self.assertEqual(karat(2,10), 20)

    def test_c(self):
        self.assertEqual(karat(1234,5678), 7006652)

    def test_d(self):
        self.assertEqual(karat(3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497757247093699959574966967627), 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184)

    def test_e(self):
        self.assertEqual(karat(-1234,5678), -7006652)
if __name__ == '__main__':
    unittest.main()
