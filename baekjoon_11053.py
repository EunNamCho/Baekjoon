#dp, LIS
#Binary_search로도 풀 수 있음.
import sys


n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().strip().split()))
dp = [1 for i in range(len(a))]
for i in range(len(a)):
    for k in range(i):
        if a[i] > a[k]:
            dp[i] = max(dp[i], dp[k]+1)
print(max(dp))
