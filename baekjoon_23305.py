import sys
from collections import defaultdict

N = int(sys.stdin.readline())
have = list(map(int, sys.stdin.readline().strip().split()))
want = list(map(int, sys.stdin.readline().strip().split()))
h_dict, w_dict = defaultdict(int), defaultdict(int)
for idx, elem in enumerate(have):
    h_dict[have[idx]] += 1
    w_dict[want[idx]] += 1
for idx, elem in enumerate(have):
    if have[idx] == want[idx]:
        h_dict[have[idx]] -= 1
        w_dict[want[idx]] -= 1
for key, value in w_dict.items():
    if h_dict.get(key) is not None:
        if h_dict.get(key) - w_dict.get(key) >= 0:
            h_dict[key] -= w_dict[key]
        else:
            h_dict[key] = 0
print(sum(h_dict.values()))
