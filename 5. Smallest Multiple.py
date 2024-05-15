""" 1 = 1
2 = 2
3 = 6
4 = 2*2 = 12 
5 = 60 (prime)
6 = 3*2 = 60
7 = 420 (prime)
8 = 2*2* 2 = 840 (new)
9 = 3*3 = 2520
10 = 2*5 = 2520
11 = 27720
12 = 2*2*3 = 27720 (exists)
13 = 27720*13
14 = 2*7 = do nothing
15 = do nothing
16 = 2*2*2*2 (mul 2) """


import math

#if num is prime, multiply
#if num is not prime, check if divisible otherwise mul smallest prime

def factor(n):
    if (n % 2 == 0):
        return 2
    i = 3
    while (i * i <= n):
        if (n % i == 0):
            return i
        i += 2

    return n

def prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i == 0):
            return False
    return True


def find(max):
    ans = 1
    for i in range(1, max):
        if prime(i):
            ans = ans * i
        else:
            if ans % i != 0:
                ans = ans * factor(i)
    print(ans)


find(20)