# 이건 그냥 식 알면되는거니까
# nCr = n!/(n-r)!r!
import sys
import math

n, k = map(int, sys.stdin.readline().split())
print(math.comb(n, k))
