"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
def is_palindrome(n):
    return str(n) == str(n)[::-1]

m = 0
for i in range(999, 99, -1):
    if m >= i * 999:
        break
    for j in range(999, i, -1):
        p = i * j
        if m < p and is_palindrome(p):
            m = p

print(m)
