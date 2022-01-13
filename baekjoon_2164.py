#deque도 리스트컴프리헨션(내포)같은게 가능하다


import sys
from collections import deque


deck = deque(i for i in range(1,int(sys.stdin.readline())+1))
while True:
    if len(deck) == 1:
        break
    else:
        deck.popleft()
        deck.append(deck.popleft())
print(deck[0])