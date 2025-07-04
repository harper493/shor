
import sympy
import os
import sys
import random
import math

def factor(n):
    while True:
        sq = int(math.sqrt(n))
        a = random.randint(int(sq * 0.7), int(sq * 1.3))
        g = math.gcd(n,a)
        if g > 1:
            return (a, 0, g)
        m = a
        length = 1
        while m != 1:
            m = (m * a) % n
            length += 1
            if length % 5000000 == 0:
                print(n, a, m, length)
        if length % 2 == 1:
            print("Odd length: ", a, length)
            continue
        g = 1
        r2 = length//2
        #
        # Do first step of Euclid GCD with modular exponentiation
        #
        while r2 > 0:
            g = (g * a) % n
            r2 -= 1
        #
        # Now finish using the normal algorithm
        #
        g1 = math.gcd(n-1 if g==0 else g-1, n)
        if (g1==1 or g1==n):
            print("Bad GCD: ", a, length, g1)
        else:
            break
    return a, length, g1

while True:
    nstr = input("Number to factor: ")
    if len(nstr) > 0:
        try:
            n = int(nstr)
        except:
            continue
    if n==0:
        break
    elif sympy.isprime(n):
        print(f'{n} is prime')
    else:
        a, l, g = factor(n)
        print(f'{n} = {g} * {n//g} using a = {a} length {l} factors {sympy.factorint(n)}')