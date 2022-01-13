import sys

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().strip().split()))
S = list(set(L))
S.sort()
D = dict()
answer = []
for idx, elem in enumerate(S):
    D[elem] = str(idx)
for elem in L:
    answer.append(D[elem])
print(' '.join(answer))
