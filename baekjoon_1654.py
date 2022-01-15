import sys
import math
sys.setrecursionlimit(10**6)


def binary_search(l_point, r_point):
    mid_point = (l_point+r_point)//2
    if not mid_point:
        mid_point = 1
    global L
    temp = sum(elem//mid_point for elem in L)
    if l_point >= r_point:
        return l_point
    elif temp >= N:
        return binary_search(mid_point+1, r_point)
    elif temp < N:
        return binary_search(l_point, mid_point-1)


K, N = map(int, sys.stdin.readline().strip().split())
L = list()
for i in range(K):
    L.append(int(sys.stdin.readline()))
max_l = binary_search(0, sum(L)//N)
print(max_l)
