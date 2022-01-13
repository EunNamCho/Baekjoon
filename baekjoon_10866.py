#a,b=(1,2)같은 언패키징할 때
#개수 안맞으면 에러


import sys
from collections import deque


class Deque:
    def __init__(self):
        self.D = deque()
    def push_front(self, p_elem):
        self.D.appendleft(p_elem)
    def push_back(self, p_elem):
        self.D.append(p_elem)
    def pop_front(self):
        if len(self.D):
            print(self.D.popleft())
        else:
            print(-1)
    def pop_back(self):
        if len(self.D):
            print(self.D.pop())
        else:
            print(-1)
    def size(self):
        print(len(self.D))
    def empty(self):
        if len(self.D):
            print(0)
        else:
            print(1)
    def front(self):
        if len(self.D):
            print(self.D[0])
        else:
            print(-1)
    def back(self):
        if len(self.D):
            print(self.D[-1])
        else:
            print(-1)


test_case = int(sys.stdin.readline())
d = Deque()
for _ in range(test_case):
    my_input = sys.stdin.readline().strip().split()
    order = my_input[0]
    if order == 'push_front':
        d.push_front(my_input[1])
    elif order == 'push_back':
        d.push_back(my_input[1])
    elif order == "pop_front":
        d.pop_front()
    elif order == "pop_back":
        d.pop_back()
    elif order == "size":
        d.size()
    elif order == "empty":
        d.empty()
    elif order == "front":
        d.front()
    elif order == "back":
        d.back()