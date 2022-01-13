#15683문제의 알고리즘 활용하니까
#2400ms정도 나옴 그리고 그게 제일 빠른듯.
#늦은 사람들 코드를 보니까 다들 deepcopy를 썼음
#또 어떤 사람코드보니까 itertoolseh 사용함
#근데 여기가 노다지임
#순회도 쉽게 할 수 있고, permutation, combination등등 있음
#유용하게 쓰자.


import sys
from collections import deque


def bfs():
    temp = deque()
    global infection
    global room
    global clean
    for elem in List:
        lab[elem[0][0]][elem[0][1]] = 1
        lab[elem[1][0]][elem[1][1]] = 1
        lab[elem[2][0]][elem[2][1]] = 1
        for virus in viruses:
            temp.append(virus)
            while temp:
                x, y = temp.popleft()
                if x+1 < N and not lab[x+1][y] and not (x+1,y) in infection:
                    temp.append((x+1,y))
                    infection.add((x+1,y))
                if x-1 >= 0 and not lab[x-1][y] and not (x-1,y) in infection:
                    temp.append((x-1,y))
                    infection.add((x-1,y))
                if y+1 < M and not lab[x][y+1] and not (x,y+1) in infection:
                    temp.append((x,y+1))
                    infection.add((x,y+1))
                if y-1 >= 0 and not lab[x][y-1] and not (x,y-1) in infection:
                    temp.append((x,y-1))
                    infection.add((x,y-1))
        room = max(room, clean-3-len(infection))
        lab[elem[0][0]][elem[0][1]] = 0
        lab[elem[1][0]][elem[1][1]] = 0
        lab[elem[2][0]][elem[2][1]] = 0
        infection = set()


viruses = []
can_wall = []
infection = set()
clean = 0
room = 0
List = []
N, M = map(int, sys.stdin.readline().strip().split())
lab = []
for _ in range(N):
    lab.append(list(map(int, sys.stdin.readline().strip().split())))
for i in range(N):
    for k in range(M):
        if lab[i][k] == 2:
            viruses.append((i,k))
        elif not lab[i][k]:
            can_wall.append((i,k))
            clean += 1
for i in range(len(can_wall)):
    for k in range(i+1, len(can_wall)):
        for j in range(k+1, len(can_wall)):
            List.append([can_wall[i], can_wall[k], can_wall[j]])
bfs()
print(room)