import sys
import math
sys.setrecursionlimit(10**6)


def binary_search(l_point, r_point, count):
    mid_point = math.floor((l_point+r_point)/2)
    global L
    temp = 0
    answer = 0
    for idx, elem in enumerate(L):
        temp += math.floor(elem/mid_point)
    if temp > N and count != N:
        answer = binary_search(mid_point+1, r_point, temp)
    elif temp < N and count != N:
        answer = binary_search(l_point, mid_point-1, temp)
    return answer



K, N = map(int, sys.stdin.readline().strip().split())
L = list()
for _ in range(K):
    L.append(int(sys.stdin.readline()))
max_l = math.floor(sum(L)/N)
max_l = binary_search(math.floor(max_l/2), max_l, 0)
print(max_l)
