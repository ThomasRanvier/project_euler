"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
from math import sqrt
from itertools import count, islice

def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))

def prime(l):
    c = 2
    n = 0
    while c < l:
        n += 6
        if is_prime(n + 1):
            c += 1
        if is_prime(n - 1):
            c += 1
    return n + 1

print(prime(10001))
