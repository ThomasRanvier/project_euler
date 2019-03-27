"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
import math

c = {}

def divisors(n):
    global c
    if n in c:
        return c[n]
    divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            divisors.append(i)
            if i*i != n:
                divisors.append(n / i)
    c[n] = sum(divisors) - n
    return c[n]

a = set()
for i in range(1, 10000 + 1):
    v = divisors(i)
    if i != v and i == divisors(v):
        a.add(i)
        a.add(v)
print(sum(a))
