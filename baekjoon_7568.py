import sys


N = int(sys.stdin.readline())
people = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
rank = [0]*N
for i in range(len(people)):
    for j in range(i+1, len(people)):
        if people[i][0] > people[j][0] and people[i][1] > people[j][1]:
            rank[j] += 1
        elif people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank[i] += 1
for v in rank:
    print(v+1, end=' ')
