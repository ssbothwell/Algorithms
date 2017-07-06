#!/usr/bin/env python
import unittest
from sieve_of_eratosthenes import *

class Sieve(unittest.TestCase):
    def setUp(self):
        pass

    def test_a(self):
        self.assertEqual(sieve1(3), '3 is prime')

    def test_b(self):
        self.assertEqual(sieve1(4), '4 is composite')

    def test_c(self):
        self.assertEqual(sieve1(5), '5 is prime')

    def test_d(self):
        self.assertEqual(sieve1(6), '6 is composite')

    def test_e(self):
        self.assertEqual(sieve1(7), '7 is prime')

    def test_e(self):
        self.assertEqual(sieve1(8), '8 is composite')

    def test_f(self):
        self.assertEqual(sieve1(9), '9 is composite')

    def test_g(self):
        self.assertEqual(sieve1(10), '10 is composite')

    def test_h(self):
        self.assertEqual(sieve1(1299709), '1299709 is prime')

    def test_i(self):
        self.assertEqual(sieve1(1299708), '1299708 is composite')

if __name__ == '__main__':
    unittest.main()
