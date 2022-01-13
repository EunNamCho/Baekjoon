import sys


D = dict()
N = int(sys.stdin.readline())
for _ in range(N):
    name, state = sys.stdin.readline().strip().split()
    if state == 'enter':
        D[name] = 1
    else:
        del D[name]
D = list(D)
D.sort(reverse=True)
print('\n'.join(D))