#!/usr/bin/env python
"""
Functional Linked List
Source: https://dbader.org/blog/functional-linked-lists-in-python

A linked list implementation built on Nil and cons. Nil represents
the empty list and the cons function extends a list at the front
by inserting a new value

Lists are made up out of nested 2-Tuples.
For Example:
    [1,2,3] is represented by cons(1, cons(2, cons(3, Nil)))
    Which evaluates to (1, (2, (3, Nil)))
"""

Nil = None
def cons(x, xs=Nil):
    return (x, xs)

assert cons(0) == (0, Nil)
assert cons(0, (1, (2, Nil))) == (0, (1, (2, Nil)))

def lst(*xs):
    """
    Helper function allow an easier synax
    for list generation
    """
    if not xs:
        return Nil
    else:
        return cons(xs[0], lst(*xs[1:]))

assert lst() == Nil
assert lst(1) == (1, Nil)
assert lst(1,2,3,4) == (1, (2, (3, (4, Nil))))

def head(xs):
    """ Returns the first element of the list"""
    return xs[0]

assert head(lst(1,2,3)) == 1

def tail(xs):
    """ Returns all but the head of the list"""
    return xs[1]

assert tail(lst(1,2,3)) == lst(2,3)

def is_empty(xs):
    """ Returns True if the list has no elements """
    return xs is Nil

assert is_empty(Nil) == True
assert not is_empty(lst(1, 2, 3))

def length(xs):
    if is_empty(xs):
        return 0
    else:
        return 1 + length(tail(xs))

assert length(lst(1, 2, 3, 4)) == 4
assert length(Nil) == 0

def concat(xs, ys):
    """ Concatenate two lists recursively """
    if is_empty(xs):
        return ys
    else:
        return cons(head(xs), concat(tail(xs), ys))

assert concat(lst(1,2),lst(3,4)) == lst(1,2,3,4)

def last(xs):
    """ Return the last non-Nil element in the lst """
    if is_empty(tail(xs)):
        return head(xs)
    else:
        return last(tail(xs))

assert last(lst(1, 3, 3, 4)) == 4

def init(xs):
    """ Return all elements but the last """
    if is_empty(tail(tail(xs))):
        return cons(head(xs))
    else:
        return cons(head(xs), init(tail(xs)))

assert init(lst(1, 2, 3, 4)) == lst(1, 2, 3)

def reverse(xs):
    """ slow (n^2) list reversal """
    if is_empty(xs):
        return xs
    else:
        return concat(reverse(tail(xs)), cons(head(xs), Nil))

assert reverse(Nil) == Nil
assert reverse(cons(0, Nil)) == (0, Nil)
assert reverse(lst(1, 2, 3, 4)) == lst(4, 3, 2, 1)
assert reverse(reverse(lst(1, 2, 3, 4))) == lst(1, 2, 3, 4)

def take(n, xs):
    """ return the first n elements from the list """
    if n == 0:
        return Nil
    else:
        return cons(head(xs), take(n-1, tail(xs)))

assert take(2, lst(1, 2, 3, 4)) == lst(1, 2)

def drop(n, xs):
    """ returns everything but the first n elements """
    if n == 0:
        return xs
    else:
        return drop(n-1, tail(xs))

assert drop(1, lst(1, 2, 3)) == lst(2, 3)
assert drop(2, lst(1, 2, 3, 4)) == lst(3, 4)

def apply(i, xs):
    """ return the i'th element """
    return head(drop(i, xs))

assert apply(0, lst(1, 2, 3, 4)) == 1
assert apply(2, lst(1, 2, 3, 4)) == 3

def insert(x, xs):
    """ Inserts x into the list mainting order """
    if is_empty(xs) or x <= head(xs):
        return cons(x, xs)
    else:
        return cons(head(xs), insert(x, tail(xs)))

assert insert(0, lst(1, 2, 3, 4)) == lst(0, 1, 2, 3, 4)
assert insert(99, lst(1, 2, 3, 4)) == lst(1, 2, 3, 4, 99)
assert insert(3, lst(1, 2, 4)) == lst(1, 2, 3, 4)

def insertion_sort(xs):
    """ insertion sort """
    if is_empty(xs):
        return xs
    else:
        return insert(head(xs), insertion_sort(tail(xs)))

assert insertion_sort(lst(1, 2, 3, 4)) == lst(1, 2, 3, 4)
assert insertion_sort(lst(3, 1, 2, 4)) == lst(1, 2, 3, 4)


def to_string(xs, prefix="[", sep=", ", postfix="]"):
    """ Flatten a list into a string """
    def _to_string(xs):
        if is_empty(xs):
            return ""
        elif is_empty(tail(xs)):
            return str(head(xs))
        else:
            return str(head(xs)) + sep + _to_string(tail(xs))
    return prefix + _to_string(xs) + postfix

assert to_string(lst(1, 2, 3, 4)) == "[1, 2, 3, 4]"

