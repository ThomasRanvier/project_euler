"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from math import sqrt
from itertools import count, islice

def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))

def primes_under(l):
    n = 0
    p = [2, 3]
    while n < l:
        n += 6
        if is_prime(n + 1) and n + 1 < l:
            p.append(n + 1)
        if is_prime(n - 1) and n - 1 < l:
            p.append(n - 1)
    return p

print(sum(primes_under(2000000)))
