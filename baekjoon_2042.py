#세그먼트 트리


import sys
import math


class S_Tree:
    def __init__(self, a_size):
        self.L = [None] * a_size
        self.hap = 0

    def insert(self, a_l, start, end, index):
        if start == end:
            self.L[index] = a_l[start]
            return self.L[index]
        mid = (start + end) // 2
        self.L[index] = self.insert(a_l, start, mid, index * 2) + self.insert(a_l, mid+1, end, index * 2 + 1)
        return self.L[index]

    def my_print(self, start, end, left, right, idx):
        if start >= left and end <= right:
            self.hap += self.L[idx]
            return
        elif end < left or start > right:
            return
        elif start == end:
            return
        mid = (start + end) // 2
        self.my_print(start, mid, left, right, idx*2)
        self.my_print(mid + 1, end, left, right, idx*2+1)

    def reset_hap(self):
        print(self.hap)
        self.hap = 0

    def find(self, start, end, target, modify):
        idx, mid = 1, 0
        while True:
            self.L[idx] += modify
            mid = (start + end) // 2
            if start == end:
                break
            elif target > mid:
                start = mid + 1
                idx = idx * 2 + 1
            elif target <= mid:
                end = mid
                idx = idx * 2


my_input = list(map(int, sys.stdin.readline().strip().split()))
s = S_Tree(2 ** (math.ceil(math.log(my_input[0], 2))+1))
elem = list()
for _ in range(my_input[0]):
    elem.append(int(sys.stdin.readline()))
s.insert(elem, 0, my_input[0]-1, 1)

for _ in range(my_input[1] + my_input[2]):
    action = list(map(int, sys.stdin.readline().strip().split()))
    if action[0] == 1:
        s.find(0, my_input[0]-1, action[1]-1, action[2]-elem[action[1]-1])
        elem[action[1]-1] = action[2]
    else:
        s.my_print(0, my_input[0]-1, action[1]-1, action[2]-1, 1)
        s.reset_hap()
