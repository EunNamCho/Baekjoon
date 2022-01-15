import sys


N = int(sys.stdin.readline())
words = list()
for i in range(N):
    temp = sys.stdin.readline().strip()
    if temp not in words:
        words.append(temp)
answer = [0]*(len(words)+1)
last = 1
for elem in words:
    answer[last] = elem
    parent = last // 2
    while True:
        if

