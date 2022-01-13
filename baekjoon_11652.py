import sys
from collections import defaultdict

N = int(sys.stdin.readline())
D = defaultdict(int)
freq = None
for _ in range(N):
    D[int(sys.stdin.readline())] += 1
for k in D.keys():
    if freq is None:
        freq = k
    elif D[k] > D[freq]:
        freq = k
    elif D[k] == D[freq]:
        if k < freq:
            freq = k
print(freq)
