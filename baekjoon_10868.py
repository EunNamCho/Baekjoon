import sys
import math

"""
def segment(idx, start, end):
    if start == end:
        S_tree[idx] = L[start]
        return S_tree[idx]
    else:
        mid = (start + end) // 2
        a, b = segment(idx * 2, start, mid), segment(idx * 2 + 1, mid + 1, end)
        if a >= b:
            S_tree[idx] = b
        else:
            S_tree[idx] = a
        return S_tree[idx]


def find(idx, start, end, d_boundary, u_boundary):
    if d_boundary <= start <= end <= u_boundary:
        return S_tree[idx]
    elif start < d_boundary <= end <= u_boundary or \
            d_boundary <= start <= u_boundary < end or \
            start < d_boundary and u_boundary < end:
        mid = (start + end) // 2
        a, b = find(idx * 2, start, mid, d_boundary, u_boundary), find(idx * 2 + 1, mid + 1, end, d_boundary, u_boundary)
        if a is None:
            return b
        elif b is None:
            return a
        elif a > b:
            return b
        else:
            return a


N, M = map(int, sys.stdin.readline().strip().split())
L = []
S_tree = [None] * pow(2, math.ceil(math.log(N, 2)) + 1)
for _ in range(N):
    L.append(int(sys.stdin.readline()))
segment(1, 0, N - 1)
for _ in range(M):
    a, b = map(lambda x: x-1, map(int, sys.stdin.readline().strip().split()))
    print(find(1, 0, N - 1, a, b))
"""

input = sys.stdin.readline
inf = 1e10


class SegTree:
    def __init__(self, n, seq):
        self.min_tree = [inf] * (2 * n)
        self.min_tree[n:] = seq[1:]
        for i in range(n - 1, 0, -1):
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


n, m = map(int, input().split())
seq = [0]
for _ in range(n):
    seq.append(int(input()))
tree = SegTree(n, seq)
for _ in range(m):
    a, b = map(int, input().split())
    print(tree.find_min(a + n - 1, b + n - 1))