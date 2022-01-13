#리스트로 초과떠서 딕셔너리 씀


import sys
from collections import defaultdict


size_1, size_2 = map(int, sys.stdin.readline().strip().split())
Dict, answer = defaultdict(int), list()
for _ in range(size_1):
    Dict[sys.stdin.readline().strip()] += 1
for _ in range(size_2):
    Dict[sys.stdin.readline().strip()] += 1
for k, v in Dict.items():
    if v == 2:
        answer.append(k)
answer.sort()
print(len(answer))
for a in answer:
    print(a)