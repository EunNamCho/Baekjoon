import sys
from collections import deque


N = int(sys.stdin.readline())
L = [i for i in range(N+1)]
S = deque()
for i in range(N-1):
    a, b = map(int, sys.stdin.readline().strip().split())
    S.append((a, b))
while S:
    a, b = S.popleft()
    if a == 1:
        L[b] = a
    elif b == 1:
        L[a] = b
    elif L[a] != a and L[b] == b:
        L[b] = a
    elif L[b] != b and L[a] == a:
        L[a] = b
    else:
        S.append((a, b))
for i in range(2, N+1):
    print(L[i])
