import sys


n, m = map(int, sys.stdin.readline().split())
q, r = divmod(n, m)
print(q)
print(r)