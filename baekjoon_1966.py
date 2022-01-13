#deque 복사 copy.deepcopy(객체)도 가능하고
#객체 = collections.deque(itertools.islice,~~~)해서
#사용하던데 이해하기 귀찮아서 다음에 찾아보는걸로


import sys, copy
from collections import deque


test_case = int(sys.stdin.readline())

for _ in range(test_case):
    size, target = map(int, sys.stdin.readline().strip().split())
    deck = deque()
    answer = list()
    elem = list(map(int, sys.stdin.readline().strip().split()))
    for k, v in enumerate(elem):
        deck.append((v, k))
    target = deck[target]
    while deck:
        max_value = max(deck)[0]
        if max_value == deck[0][0]:
            answer.append(deck.popleft())
        else:
            deck.append(deck.popleft())
    print(answer.index(target) + 1)