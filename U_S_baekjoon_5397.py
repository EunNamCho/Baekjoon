import sys
from collections import deque
#맨 마지막꺼가 정답임
#다른 건 다 시간초과

"""
class Node:
    def __init__(self):
        self.elem = None
        self.next, self.prev = None, None

    def __del__(self):
        pass


class Iterator:
    def __init__(self, a_node):
        self.pos = a_node

    def __del__(self):
        pass

    def right(self):
        self.pos = self.pos.next

    def left(self):
        self.pos = self.pos.prev


class DLL:
    def __init__(self):
        self.header = Node()
        self.trailer = Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.iter = Iterator(self.trailer)

    def insert(self, a_elem):
        new_node = Node()
        new_node.elem = a_elem
        new_node.prev = self.iter.pos.prev
        new_node.next = self.iter.pos
        self.iter.pos.prev.next = new_node
        self.iter.pos.prev = new_node

    def delete(self):
        if self.iter.pos.prev != self.header:
            target = self.iter.pos.prev
            target.prev.next = self.iter.pos
            self.iter.pos.prev = target.prev

    def my_print(self):
        cur_node = self.header.next
        while cur_node != self.trailer:
            print(cur_node.elem, end='')
            cur_node = cur_node.next
        print()

    def right(self):
        if self.iter.pos != self.trailer:
            self.iter.right()

    def left(self):
        if self.iter.pos.prev != self.header:
            self.iter.left()


for _ in range(int(sys.stdin.readline())):
    d = DLL()
    string = sys.stdin.readline().strip()
    for char in string:
        if char.isalnum():
            d.insert(char)
        else:
            if char == "<":
                d.left()
            elif char == ">":
                d.right()
            elif char == "-":
                d.delete()
    d.my_print()

for _ in range(int(sys.stdin.readline())):
    idx = 0
    answer = ""
    string = sys.stdin.readline().strip()
    for char in string:
        if char.isalnum():
            if not idx:
                answer = answer + char
            else:
                answer = answer[:idx] + char + answer[idx:]
        else:
            if char == "<":
                if abs(idx) < len(answer):
                    idx -= 1
            elif char == ">":
                if idx < 0:
                    idx += 1
            elif char == "-":
                if answer and abs(idx) < len(answer):
                    if not idx:
                        answer = answer[:-1]
                    else:
                        answer = answer[:idx-1] + answer[idx:]
    print(answer)
"""
for _ in range(int(sys.stdin.readline())):
    left, right = deque(), deque()
    string = sys.stdin.readline()
    for char in string:
        if char.isalnum():
            left.append(char)
        else:
            if char == "<":
                if left:
                    right.appendleft(left.pop())
            elif char == ">":
                if right:
                    left.append(right.popleft())
            elif char == "-":
                if left:
                    left.pop()
    print(''.join(left) + ''.join(right))
