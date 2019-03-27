"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
#Easy way
from itertools import permutations
print([i for i in permutations(range(10))][999999])

#Other way
def permut(v):
    if len(v) <= 1:
        return [v]
    perm = []
    for i in range(len(v)):
        m = v[i]
        r = v[:i] + v[i+1:]
        for p in permut(r):
            perm.append([m] + p)
    return perm
    
values = [i for i in range(10)]
print(permut(values)[999999])
