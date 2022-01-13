import heapq
import sys


N = int(sys.stdin.readline())
H = []
answer = 0
for _ in range(N):
    heapq.heappush(H,int(sys.stdin.readline()))
while len(H) != 1:
    a = heapq.heappop(H) + heapq.heappop(H)
    answer += a
    heapq.heappush(H,a)
print(answer)