#굳이 힙을 쓸 필요가 없을 것 같음.
#대신 answer에 하나씩 더할때는 매번 sort할 수 가 없으니
#heap을 이용
#sort에 매개변수 key가 있는데, 여기에는 함수를 넣어준다.
#정렬할때 원소들에 적용할 함수를 전달함.
#대소문자 상관없이 정렬하고싶다면, key=str.lower이렇게

import sys
import heapq as h

N, K = map(int, sys.stdin.readline().strip().split())
jewelry, bag = [], []
steal = []
answer = 0
for _ in range(N):
    jewelry.append(list(map(int, sys.stdin.readline().strip().split())))
for _ in range(K):
    bag.append(int(sys.stdin.readline()))
bag.sort()
for b in bag:
    while jewelry and jewelry[0][0] <= b:
        h.heappush(steal, -h.heappop(jewelry)[1])
    if steal:
        answer -= h.heappop(steal)
    if not jewelry:
        break
print(answer)



"""
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
N, K = map(int, input().split())
jowel = [tuple(map(int, input().split())) for _ in range(N)]
jowel.sort(key=lambda x: x[0], reverse=True)
bag = [int(input()) for _ in range(K)]
bag.sort()
result = [0 for _ in range(K)]

Q = []
for i in range(K):
    while jowel and jowel[-1][0] <= bag[i]:
        heappush(Q, -jowel.pop()[1])
    if Q:
        result[i] = -heappop(Q)
print(sum(result))
"""