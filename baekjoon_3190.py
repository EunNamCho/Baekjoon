#핵심은 뱀의 이동경로를 덱에 저장하기.


import sys, pprint
from collections import deque


size = int(sys.stdin.readline()) + 2
matrix, snake, act = list(), deque(), deque()
collision = False
direction = (0, 1)
snake.append((1, 1))
time = 0
for i in range(size):
    matrix.append(list())
for i in range(size):
    for k in range(size):
        if i == 0 or i == size - 1 or k == 0 or k == size - 1:
            matrix[i].append(True)
        else:
            matrix[i].append(False)
for _ in range(int(sys.stdin.readline())):
    pos = list(map(int, sys.stdin.readline().strip().split()))
    matrix[pos[0]][pos[1]] = 'apple'
matrix[1][1] = True
for _ in range(int(sys.stdin.readline())):
    act.append(sys.stdin.readline().strip().split())
while act:
    action = act.popleft()
    while int(action[0]) > time:
        way = (snake[-1][0] + direction[0], snake[-1][1] + direction[1])
        time += 1
        if matrix[way[0]][way[1]] and matrix[way[0]][way[1]] != 'apple':
            collision = True
            break
        else:
            if matrix[way[0]][way[1]] == 'apple':
                pass
            else:
                tail = snake.popleft()
                matrix[tail[0]][tail[1]] = False
            matrix[way[0]][way[1]] = True
            snake.append(way)
    if collision:
        break
    elif action[1] == "L":
        if direction == (0, 1):
            direction = (-1, 0)
        elif direction == (0, -1):
            direction = (1, 0)
        elif direction == (1, 0):
            direction = (0, 1)
        elif direction == (-1, 0):
            direction = (0, -1)
    elif action[1] == "D":
        if direction == (0, 1):
            direction = (1, 0)
        elif direction == (0, -1):
            direction = (-1, 0)
        elif direction == (1, 0):
            direction = (0, -1)
        elif direction == (-1, 0):
            direction = (0, 1)
if collision:
    print(time)
else:
    while True:
        way = (snake[-1][0] + direction[0], snake[-1][1] + direction[1])
        time += 1
        if matrix[way[0]][way[1]] and matrix[way[0]][way[1]] != 'apple':
            print(time)
            break
        else:
            if matrix[way[0]][way[1]] == 'apple':
                pass
            else:
                tail = snake.popleft()
                matrix[tail[0]][tail[1]] = False
            matrix[way[0]][way[1]] = True
            snake.append(way)