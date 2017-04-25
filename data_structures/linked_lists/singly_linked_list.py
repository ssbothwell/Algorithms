#!/usr/bin/env python
"""
Class Based Singly Linked List Implementation
"""

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class Linked_List(object):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.size = 0

    def display(self):
        current = self.head
        while current is not None:
            print current.data, " -> ",
            current = current.get_next()
        print []

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next_node = new_node
        self.tail = new_node
        self.size += 1

    def length(self):
        return self.size

    def search(self, data):
        current = self.head
        found = False
        while self.tail != current:
            if current.data == data:
                found = True
                break
            else:
                current = current.get_next()
        if found == False:
            return ValueError("data not in list")
        return current.data

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while found == False:
            if current.data == data:
                found = True
                break
            else:
                previous = current
                current = current.get_next()
        if current is None:
            return ValueError("data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


if __name__ == '__main__':
    l = Linked_List()
    l.append(1)
    l.append(3)
    l.append(2)
    l.append(4)
    l.display()
    print l.length()
