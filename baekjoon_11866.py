import sys
from collections import deque


size, hash = sys.stdin.readline().strip().split()
deck = list(i for i in range(1, int(size) + 1))
answer = deque()
hash = int(hash)
idx = 0
while deck:
    idx = (idx + hash - 1) % len(deck)
    answer.append(str(deck.pop(idx)))
string = ', '.join(answer)
print('<' + string + '>')