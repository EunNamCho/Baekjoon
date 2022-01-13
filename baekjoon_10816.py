#처음에는 리스트로 할라했는데 시간초과 떠서
#그냥 딕셔너리로 품


import sys
from collections import defaultdict

'''
size = int(sys.stdin.readline())
List = list(map(int, sys.stdin.readline().strip().split()))
size = int(sys.stdin.readline())
question = list(map(int, sys.stdin.readline().strip().split()))
answer = list()
for q in question:
    answer.append(List.count(q))
for a in answer:
    print(a, end=' ')
'''
size = int(sys.stdin.readline())
Dict = defaultdict(int)
for i in (map(int, sys.stdin.readline().strip().split())):
   Dict[i] += 1
size = int(sys.stdin.readline())
question = list(map(int, sys.stdin.readline().strip().split()))
answer = [(q, Dict[q]) for q in question]
for a in answer:
    print(a[-1], end=' ')