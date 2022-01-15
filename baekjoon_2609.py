# normal and optimal
import sys


def gcd(a, b):
    q, r = divmod(a, b)
    if not r:
        return b
    else:
        return gcd(b, r)


a, b = map(int, sys.stdin.readline().split())
if a >= b:
    g = gcd(a, b)
else:
    g = gcd(b, a)
lcm = a*b//g
print(g)
print(lcm)
