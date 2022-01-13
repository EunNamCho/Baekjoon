import sys


class Iterator:
    def __init__(self, p_node):
        self.position = p_node

    def move_r(self):
        self.position = self.position.n_node

    def move_l(self):
        self.position = self.position.p_node


class Node:
    def __init__(self):
        self.elem = None
        self.n_node, self.p_node = None, None

    def __del__(self):
        pass


class Sequence:
    def __init__(self):
        self.header, self.trailer = Node(), Node()
        self.header.n_node = self.trailer
        self.trailer.p_node = self.header
        self.pos = Iterator(self.trailer)

    def insert(self, p_elem):
        node = Node()
        node.elem = p_elem
        node.n_node = self.pos.position
        node.p_node = self.pos.position.p_node
        self.pos.position.p_node.n_node = node
        self.pos.position.p_node = node

    def delete(self):
        if self.pos.position.p_node != self.header:
            self.pos.position.p_node.p_node.n_node = self.pos.position
            self.pos.position.p_node = self.pos.position.p_node.p_node


    def my_print(self):
        cur_node = self.header.n_node
        while cur_node != self.trailer:
            print(cur_node.elem, end='')
            cur_node = cur_node.n_node
        print()

    def i_moving(self, direction):
        if direction == "L":
            if self.pos.position.p_node != self.header:
                self.pos.move_l()
        else:
            if self.pos.position != self.trailer:
                self.pos.move_r()

s = Sequence()
for char in sys.stdin.readline().strip():
    s.insert(char)
for _ in range(int(sys.stdin.readline())):
    act = sys.stdin.readline().strip().split()
    if act[0] == "P":
        s.insert(act[1])
    elif act[0] == "D":
        s.i_moving("D")
    elif act[0] == "L":
        s.i_moving("L")
    elif act[0] == "B":
        s.delete()
s.my_print()