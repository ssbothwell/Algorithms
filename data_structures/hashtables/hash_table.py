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
        hash_value = self.hash_function(key, len(self.slots))
        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data
            else:
                nextslot = self.rehash(hash_value, len(self.slots))
                while self.slots[nextslot] != None and \
                            self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))
                    if nextslot == hash_value:
                        self.slots += [None] * self.size
                        self.data += [None] * self.size
                        self.size *= 2

            if self.slots[nextslot] == None:
                self.slots[nextslot] = key
                self.data[nextslot] = data
            else:
                self.data[nextslot] = data

    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] != None and \
                            not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position,len(self.slots))
                if position == start_slot:
                    stop = True
        return data

    def delete(self, key):
        hash_value = self.hash_function(key, len(self.slots))
        if self.slots[hash_value] == key:
            self.slots[hash_value] = None
            self.data[hash_value] = None
        return

    def length(self):
        return self.size

    def hash_function(self, key, size):
        return hash(key)%size

    def rehash(self, oldhash, size):
        return (oldhash+1)%size

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.insert(key, data)

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


if __name__ == '__main__':
    H = hash_table()
    H['foo'] = 'bar'
    H['baz'] = 'bam'
    print(H['foo'])
