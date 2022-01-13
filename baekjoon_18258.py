#이 문제 list로 푸니까 시간초과 뜸
#내 예상은 아마도 pop때문인듯

import sys
from collections import deque

class Queue:
    def __init__(self):
        self.s = 0
        self.List = deque()

    def push(self, p_elem):
        self.List.append(p_elem)
        self.s += 1

    def pop(self):
        if self.s:
            print(self.List[0])
            self.List.popleft()
            self.s -= 1
        else:
            print(-1)

    def size(self):
        print(self.s)

    def empty(self):
        if self.s:
            print(0)
        else:
            print(1)

    def front(self):
        if self.s:
            print(self.List[0])
        else:
            print(-1)

    def back(self):
        if self.s:
            print(self.List[-1])
        else:
            print(-1)


Q = Queue()
for _ in range(int(sys.stdin.readline())):
    order = sys.stdin.readline().strip().split()
    if order[0] == 'push':
        Q.push(int(order[-1]))
    elif order[0] == 'pop':
        Q.pop()
    elif order[0] == 'size':
        Q.size()
    elif order[0] == 'empty':
        Q.empty()
    elif order[0] == 'front':
        Q.front()
    elif order[0] == 'back':
        Q.back()