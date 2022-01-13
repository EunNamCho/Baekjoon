import sys, heapq
from collections import defaultdict


Dict = defaultdict(list)
earn = 0
for _ in range(int(sys.stdin.readline())):
    pay, deadline = map(int, sys.stdin.readline().strip().split())
    heapq.heappush(Dict[deadline], (-pay, pay))
for k in Dict.keys():
    earn += heapq.heappop(Dict[k])[1]
print(earn)