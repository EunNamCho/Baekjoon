import sys


N, M = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))

count = 0
lo, hi = 0, 1
temp = arr[lo]
while lo < N:
    if temp == M:
        count += 1
        temp -= arr[lo]
        lo += 1
    if hi == N and temp < M:
        break
    elif temp < M:
        temp += arr[hi]
        hi += 1
    elif temp > M:
        temp -= arr[lo]
        lo += 1
print(count)