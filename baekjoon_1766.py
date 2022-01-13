"""
pypy3로 푸니까 correct
python3은 시간초과
in_degree는 정점을 저장할 필요가 없는데
유지하고 있었음. 그냥 정수로 +=1 -=1하면 됐는데
"""
import sys
import heapq
from collections import deque


N, M = map(int, sys.stdin.readline().split())
D = dict()
H = list()
for i in range(1, N+1):
    #[[in], [out]]
    D[i] = [0, []]
for _ in range(M):
    in_degree, out_degree = map(int, sys.stdin.readline().strip().split())
    D[in_degree][1].append(out_degree)
    D[out_degree][0] += 1
for i in range(1, N+1):
    if not D[i][0]:
        heapq.heappush(H, i)
while H:
    elem = heapq.heappop(H)
    for k in range(len(D[elem][1])):
        D[D[elem][1][k]][0] -= 1
        if not D[D[elem][1][k]][0]:
            heapq.heappush(H, D[elem][1][k])
    print(elem, end=' ')

