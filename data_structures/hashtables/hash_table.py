#!/usr/bin/env python
"""
Hash Table Data Structure

An unordered associative array data structure which maps
keys to values. Hash tables use a hashing function to
generate an index value in an array where the desired value
is stored.

In ideal conditions the hashing function will assign a
unique index value for each key. A perfect hashing function
is rarely possible and so most hash tables must accomdate
for potential collisions caused by imperfect hash functions.

Example Hashing Functions:
    -Remainder Method:  key % size of bucket array.
    -Folding Method:    split key into chunks, sum chunks
                        then apply remainder method.
    -Mid Square Method: Square the value, then aplpy the
                        remainder method on the middle
                        two values of the square.

To apply a hashing function to a string, simlpy convert
the characters to a sequence of ordinal values.

Average Performance:
Space   O(n)
Search  O(1)
Insert  O(1)
Delete  O(1)
"""
class hash_table:

    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def insert(self, key, data):
        hash_value = hash_value(key, len(self.slots))
        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_velue] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data
            else:
                nextslot = self.rehash(hash_value, len(self.slots))
                while self.slots[nextslot] != None and \
                            self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

            if self.slots[nextslot] = None:
                self.slots[nextslot] = key
                self.data[nextslot] = data
            else:
                self.data[nextslot] = data

    def get(self, key):
        return

    def delete(self, key):
        return

    def length(self):
        return self.size

    def hash_function(self, key, size):
        return

    def rehash(self, oldhash, size):
        return


def hash1(val, buckets):
    """ remainder method hash function """
    return val % buckets

def hash2(val, buckets):
    """ folding method hash function """

    val = str(val)
    h = 0
    for ch in range(0, len(val), 2):
        h += int(val[ch:ch+2])
    return h % buckets

def hash3(val, buckets):
    """ mid-square method hash function """
    h = str(val**2)
    return int(h[len(h)//2]) % buckets

def hash4(string, buckets):
    """ basic string hashing example """
    sum = 0
    for pos in range(len(string)):
        sum = sum + (ord(string[pos])*pos)
    return sum % buckets
