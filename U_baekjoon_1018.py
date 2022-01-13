import sys
import pprint


col, row = map(int, sys.stdin.readline().strip().split())
string = list()
start = list()
modify = 0
for _ in range(col):
    string.append(sys.stdin.readline().strip())
for _ in range(col):
    for i in range(row-7):
        pass
for i in range(col):
    start.append(string[i][0])
st = start[0]
for i in range(len(start)):
    if start[i] != st:
        start[i] = st
        modify += 1
    if st == "W":
        st = "B"
    else:
        st = "W"
for i, s_str in enumerate(string):
    word = start[i]
    for s in s_str:
        if s != word:
            modify += 1
        if word == "W":
            word = "B"
        else:
            word = "W"
print(modify)