#나는 위에서부터 내려가는 정석? 비슷한 방법
#밑에 코드는 밑에서부터 위로 올라가는 방법
#시간은 밑에 코드가 압도적으로 빨랐음


import sys
import math


def d_segment(idx, start, end):
    if start == end:
        S_tree1[idx] = L[start]
        return S_tree1[idx]
    else:
        mid = (start + end) // 2
        a, b = d_segment(idx * 2, start, mid), d_segment(idx * 2 + 1, mid + 1, end)
        if a > b:
            S_tree1[idx] = b
        else:
            S_tree1[idx] = a
        return S_tree1[idx]


def d_find(idx, start, end, d_boundary, u_boundary):
    mid = (start + end) // 2
    if d_boundary <= start and end <= u_boundary:
        return S_tree1[idx]
    elif start < d_boundary <= end <= u_boundary or \
            d_boundary <= start <= u_boundary < end or \
            start < d_boundary and u_boundary < end:
        a = d_find(idx * 2, start, mid, d_boundary, u_boundary)
        b = d_find(idx * 2 + 1, mid + 1, end, d_boundary, u_boundary)
        if a is None and b is not None:
            return b
        elif a is not None and b is None:
            return a
        elif a > b:
            return b
        else:
            return a
    else:
        return


def u_segment(idx, start, end):
    if start == end:
        S_tree2[idx] = L[start]
        return S_tree2[idx]
    else:
        mid = (start + end) // 2
        a, b = u_segment(idx * 2, start, mid), u_segment(idx * 2 + 1, mid + 1, end)
        if a > b:
            S_tree2[idx] = a
        else:
            S_tree2[idx] = b
        return S_tree2[idx]


def u_find(idx, start, end, d_boundary, u_boundary):
    mid = (start + end) // 2
    if d_boundary <= start and end <= u_boundary:
        return S_tree2[idx]
    elif start < d_boundary <= end <= u_boundary or \
            d_boundary <= start <= u_boundary < end or \
            start < d_boundary and u_boundary < end:
        a = u_find(idx * 2, start, mid, d_boundary, u_boundary)
        b = u_find(idx * 2 + 1, mid+1, end, d_boundary, u_boundary)
        if a is None and b is not None:
            return b
        elif a is not None and b is None:
            return a
        elif a > b:
            return a
        else:
            return b
    else:
        return


N, M = map(int, sys.stdin.readline().strip().split())
L, answer = [], []
for i in range(N):
    L.append(int(sys.stdin.readline()))
S_tree1 = [None] * pow(2, math.ceil(math.log(N, 2))+1)
S_tree2 = [None] * pow(2, math.ceil(math.log(N, 2))+1)
d_segment(1, 0, N-1)
u_segment(1, 0, N-1)
for _ in range(M):
    down, up = map(lambda x: x-1, map(int, sys.stdin.readline().strip().split()))
    print(d_find(1, 0, N-1, down, up), u_find(1, 0, N-1, down, up))


"""
import sys, math

input = sys.stdin.readline
inf = 1e10

class SegTree:
    def __init__(self, n, seq):
        self.min_tree = [inf] * (2 * n)
        self.min_tree[n:] = seq[1:]
        self.max_tree = [0] * (2 * n)
        self.max_tree[n:] = seq[1:]
        for i in range(n - 1, 0, -1):
            self.max_tree[i] = max(self.max_tree[i * 2], self.max_tree[i * 2 + 1])
            self.min_tree[i] = min(self.min_tree[i * 2], self.min_tree[i * 2 + 1])

    def find_min(self, st, end):
        r = inf
        while st <= end:
            if st % 2 == 1:
                r = min(r, self.min_tree[st])
                st += 1
            if end % 2 == 0:
                r = min(r, self.min_tree[end])
                end -= 1
            st //= 2
            end //= 2
        return r

    def find_max(self, st, end):
        r = 0
        while st <= end:
            if st % 2 == 1:
                r = max(r, self.max_tree[st])
                st += 1
            if end % 2 == 0:
                r = max(r, self.max_tree[end])
                end -= 1
            st //= 2
            end //= 2
        return r


n, m = map(int, input().split())
seq = [0]
for _ in range(n):
    seq.append(int(input()))
    
tree = SegTree(n, seq)
for _ in range(m):
    a, b = map(int, input().split())
    minimum = tree.find_min(a + n - 1, b + n - 1)
    maximum = tree.find_max(a + n - 1, b + n - 1)
    print(minimum, maximum)

"""