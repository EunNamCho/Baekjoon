import sys
import heapq


max_heap = list()
min_heap = list()
for _ in range(int(sys.stdin.readline())):
    elem = int(sys.stdin.readline())
    if not max_heap:
        heapq.heappush(max_heap, (-elem, elem))
        print(max_heap[0][1])
    elif len(max_heap) > len(min_heap):
        heapq.heappush(min_heap, elem)
        if min_heap[0] < max_heap[0][1]:
            a, b = heapq.heappop(max_heap), heapq.heappop(min_heap)
            heapq.heappush(max_heap, (-b, b))
            heapq.heappush(min_heap, a[1])
        if min_heap[0] > max_heap[0][1]:
            print(max_heap[0][1])
        else:
            print(min_heap[0])
    elif len(max_heap) < len(min_heap):
        heapq.heappush(max_heap, (-elem, elem))
        if min_heap[0] < max_heap[0][1]:
            a, b = heapq.heappop(max_heap), heapq.heappop(min_heap)
             heapq.heappush(max_heap, (-b, b))
            heapq.heappush(min_heap, a[1])
        if min_heap[0] > max_heap[0][1]:
            print(max_heap[0][1])
        else:
            print(min_heap[0])
    elif len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, (-elem, elem))
        if max_heap[0][1] > min_heap[0]:
            print(min_heap[0])

        else:
            print(max_heap[0][1])
