#sys.stdin.readline안하니까
#시간초과 떴음

#heap-sort이용

import heapq
import sys
test_case = int(sys.stdin.readline())
heap = list()
for case in range(test_case):
    heapq.heappush(heap, int(sys.stdin.readline()))
for _ in range(len(heap)):
    print(heapq.heappop(heap))