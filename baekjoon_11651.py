# average optimal
import sys


positions = list()
for _ in range(int(sys.stdin.readline())):
    positions.append(tuple(map(int, sys.stdin.readline().split())))
positions.sort(key=lambda x: (x[1], x[0]))
for position in positions:
    print(position[0], position[1])
