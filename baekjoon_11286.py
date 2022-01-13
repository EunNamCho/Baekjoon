import sys, heapq
from collections import defaultdict


heap = defaultdict(list)
copy = list()
for _ in range(int(sys.stdin.readline())):
    elem = int(sys.stdin.readline())
    if elem:
        heapq.heappush(copy, abs(elem))
        heapq.heappush(heap[abs(elem)], elem)
    else:
        try:
            print(heapq.heappop(heap[heapq.heappop(copy)]))
        except:
            print(0)