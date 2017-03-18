#!/usr/bin/env python
import unittest
from strassensAlgorithm import *
from matrixAddition import addMatrix
from matrixSubtraction import subtractMatrix

class strassen(unittest.TestCase):
    def setUp(self):
        self.a = [
                    [1,2,3,4],
                    [5,6,7,8],
                    [9,10,11,12],
                    [13,14,15,16]
                    ]
        self.b = [
                    [1,2,3,4],
                    [5,6,7,8],
                    [9,10,11,12],
                    [13,14,15,16]
                    ]
        self.answer = [
                    [90,100,110,120],
                    [202,228,254,280],
                    [314,356,398,440],
                    [426,484,542,600]
                    ]

    def test_a(self):
        self.assertEqual(strassen(self.a,self.b), self.answer)


if __name__ == '__main__':
    unittest.main()
