#!/usr/bin/env python
"""
Prime Calculator using trial division

Given an input number n, check whether any prime integer
m from 2 to √n evenly divides n. If n is divisible by any
m then n is composite, otherwise it is prime.

"""
from math import sqrt
from pyutils import *

@timeit
def prime_check(n: int):
    primes = [2]
    for num in range(2,n+1):
        sqrtn = sqrt(num)
        prime_val = True
        primes_sublist = ((num, prime) for prime in primes if prime <= sqrtn)
        prime_factors = filter(lambda x: x[0] % x[1] == 0, primes_sublist)
        if any(True for _ in prime_factors) == True:
            prime_val = False
        if prime_val == True:
            primes.append(num)
    return "%s is %s" % (n, "Prime" if n in primes else "Composite")


if __name__ == '__main__':
    print(prime_check(100000))
