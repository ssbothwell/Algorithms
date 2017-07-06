#!/usr/bin/env python
"""
Prime Calculator

Sieve of Eratosthenes
    1. Create list A from 2..n
    2. Let P equal 2
    3. Enumerate the multiples of p up to n and filter
        them from A
    4. Assign the first number >p as p. Repeat step 3
        until p >= √n
    5. The remaining list A will be the primes up to n

Segmented Sieve:
    1. Divide the range 2..n into chunks of size Δ ≤ √n
    2. Find the primes in the first chunk using the
        standard sieve.
    3. For each following chunk, remove any elements that
        are multiples of the primes found in step 2.

"""
import numpy
from math import sqrt, ceil
from pyutils import timeit


@timeit
def sieve1(n: int):
    A = numpy.ones(n+1, dtype=numpy.bool)
    A[:2] = False
    A[4::2] = False
    for p in range(3, 1+ceil(sqrt(n)), 2):
        if A[p]:
            A[p*p::2*p] = False
    return "%s is %s" % (n, "prime" if n in A.nonzero()[0] else "composite")


@timeit
def sieve2(n):
    """Return an array of the primes below n."""
    prime = numpy.ones(n//3 + (n%6==2), dtype=numpy.bool)
    for i in range(3, int(n**.5) + 1, 3):
        if prime[i // 3]:
            p = (i + 1) | 1
            prime[       p*p//3     ::2*p] = False
            prime[p*(p-2*(i&1)+4)//3::2*p] = False
    result = (3 * prime.nonzero()[0] + 1) | 1
    result[0] = 3
    return numpy.r_[2,result]


@timeit
def segmented_sieve(n: int):
    delta = ceil(sqrt(n))
    chunks = [list(range(2, n+1)[x:x+delta]) for x in range(delta, n-1, delta)]
    sieve_list = [k for k,v in sieve(delta).items() if v == True]
    for i, chunk in enumerate(chunks):
        for prime in sieve_list:
            multiples = list(filter(lambda x: x >= chunk[0],
                                range(prime, chunk[-1]+1, prime)))
            chunks[i] = list(filter(lambda x: x not in multiples, chunks[i]))
            #for m in multiples:
            #    if m in chunks[i]:
            #        chunks[i].remove(m)
    #print(chunks)


if __name__ == '__main__':
    print(sieve1(1299709))
    print(sieve2(1299709))
    #print(sieve6(100000000))
    #print(sieve8(1000000000))
