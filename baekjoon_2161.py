import sys
from collections import deque

N = int(sys.stdin.readline())
L = deque(i for i in range(1, N+1))
while len(L) != 1:
    print(L.popleft(), end=' ')
    L.append(L.popleft())
print(L.pop())