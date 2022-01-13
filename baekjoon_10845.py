#from queue import Queue 가 있다.
#put, get을 이용한다.
#deque와 queue는 내부적으로 연결리스트로 구현되어 있기때문에
#인덱스 접근은 O(n)time이다.


import sys
from collections import deque


class Queue:
    def __init__(self):
        self.Q = deque()
    def push(self, p_elem):
        self.Q.append(p_elem)
    def pop(self):
        if not(self.Q):
            print(-1)
        else:
            print(self.Q.popleft())
    def size(self):
        print(len(self.Q))
    def empty(self):
        if not(self.Q):
            print(1)
        else:
            print(0)
    def front(self):
        if not(self.Q):
            print(-1)
        else:
            print(self.Q[0])
    def back(self):
        if not(self.Q):
            print(-1)
        else:
            print(self.Q[-1])


test_case = int(sys.stdin.readline())
Q = Queue()
for _ in range(test_case):
    my_input = sys.stdin.readline().strip().split()
    if my_input[0] == "push":
        Q.push(my_input[-1])
    elif my_input[0] == "pop":
        Q.pop()
    elif my_input[0] == "size":
        Q.size()
    elif my_input[0] == "empty":
        Q.empty()
    elif my_input[0] == "front":
        Queue.front(Q)
    elif my_input[0] == "back":
        Q.back()

