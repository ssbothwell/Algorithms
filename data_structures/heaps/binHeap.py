#!/usr/bin/python

"""

Binary Heap Data Structures

"""

class min_heap:
    def __init__(self):
        self.heap_list = [0]
        self.currentSize = 0

    def perc_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                tmp = self.heap_list[i // 2]
                self.heap_list[ i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp
            i = i // 2

    def insert(self, k):
        self.heap_list.append(k)
        self.currentSize = self.currentSize + 1
        self.perc_up(self.currentSize)

    def perc_down(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = tmp
            i = mc

    def min_child(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def del_min(self):
        retval = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heap_list.pop()
        self.perc_down(1)
        return retval

    def build_heap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist) 
        self.heap_list = [0] + alist[:]
        while (i > 0):
            self.perc_down(i)
            i = i - 1


class max_heap:
    def __init__(self):
        self.heap_list = [0]
        self.currentSize = 0

    def perc_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] > self.heap_list[i // 2]:
                tmp = self.heap_list[i // 2]
                self.heap_list[ i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp
            i = i // 2

    def insert(self, k):
        self.heap_list.append(k)
        self.currentSize = self.currentSize + 1
        self.perc_up(self.currentSize)

    def perc_down(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.max_child(i)
            if self.heap_list[i] < self.heap_list[mc]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = tmp
            i = mc

    def max_child(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heap_list[i * 2] > self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def del_min(self):
        retval = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heap_list.pop()
        self.perc_down(1)
        return retval

    def build_heap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heap_list = [0] + alist[:]
        while (i > 0):
            self.perc_down(i)
            i = i - 1
