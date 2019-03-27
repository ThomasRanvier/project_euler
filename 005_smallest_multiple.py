"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
i = 0
b = False
while not b:
    i += (2**3) * (3**2) * (5**1) * (7**1)
    b = True
    for a in range(1, 21):
        if i % a:
            b = False
print(i)
