"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
def lpf(a):
    b = 2
    while (a > b):
        if (a % b == 0):
            a = a / b;
            b = 2;
        else:
            b += 1;
    return b

print(lpf(600851475143))
