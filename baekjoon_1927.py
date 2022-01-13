#heapq모듈에서 heapify는 기존 리스트를 힙으로 변환


import sys, heapq

heap = list()
test_case = int(sys.stdin.readline())
for _ in range(test_case):
    number = int(sys.stdin.readline())
    if number == 0:
        if not(heap):
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, number)
