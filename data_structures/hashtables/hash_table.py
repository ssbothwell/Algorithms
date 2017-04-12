#!/usr/bin/env python

class hash_table:

    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def insert(self, key):
        key_hash = hash(key)



