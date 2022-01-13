#이 문제 빡쎘음.
#일단 if __name__ == '__main__'은
#실행시간에 영향안줌.
#브루트포스에다가 그래프이론까지 합친문제
#내가 힌트보고 짠 코드는 4800ms정도
#근데 밑에 코드는 140ms정도
#차이는 나는 매번 cctv감시경로를 색칠했고
#밑에 코드는 그냥 애초부터 감시경로를 저장함.


import sys
from copy import deepcopy
import pprint

"""
def dfs(a_idx):
    global matrix
    global area
    pos = cctv[a_idx]
    level = matrix[pos[0]][pos[1]]
    if a_idx == len(cctv)-1:
        if level == 1:
            temp = deepcopy(matrix)
            for d in direction[1]:
                p = paint(pos, *d)
                area -= p
                invisible[0] = min(invisible[0], area)
                matrix = deepcopy(temp)
                area += p
        elif level == 2:
            temp = deepcopy(matrix)
            for d in direction[2]:
                p = paint(pos, *d)
                area -= p
                invisible[0] = min(invisible[0], area)
                matrix = deepcopy(temp)
                area += p
        elif level == 3:
            temp = deepcopy(matrix)
            for d in direction[3]:
                p = paint(pos, *d)
                area -= p
                invisible[0] = min(invisible[0], area)
                matrix = deepcopy(temp)
                area += p
        elif level == 4:
            temp = deepcopy(matrix)
            for d in direction[4]:
                p = paint(pos, *d)
                area -= p
                invisible[0] = min(invisible[0], area)
                matrix = deepcopy(temp)
                area += p
        elif level == 5:
            temp = deepcopy(matrix)
            for d in direction[5]:
                p = paint(pos, *d)
                area -= p
                invisible[0] = min(invisible[0], area)
                matrix = deepcopy(temp)
                area += p
    else:
        if level == 1:
            temp = deepcopy(matrix)
            for d in direction[1]:
                p = paint(pos, *d)
                area -= p
                dfs(a_idx+1)
                area += p
                matrix = deepcopy(temp)
        elif level == 2:
            temp = deepcopy(matrix)
            for d in direction[2]:
                p = paint(pos, *d)
                area -= p
                dfs(a_idx + 1)
                area += p
                matrix = deepcopy(temp)
        elif level == 3:
            temp = deepcopy(matrix)
            for d in direction[3]:
                p = paint(pos, *d)
                area -= p
                dfs(a_idx + 1)
                area += p
                matrix = deepcopy(temp)
        elif level == 4:
            temp = deepcopy(matrix)
            for d in direction[4]:
                p = paint(pos, *d)
                area -= p
                dfs(a_idx + 1)
                area += p
                matrix = deepcopy(temp)
        elif level == 5:
            temp = deepcopy(matrix)
            for d in direction[5]:
                p = paint(pos, *d)
                area -= p
                dfs(a_idx + 1)
                area += p
                matrix = deepcopy(temp)


def paint(a_pos, a_up, a_down, a_right, a_left):
    p = 0
    if a_up:
        for i in range(a_pos[0]-1, -1, -1):
            if matrix[i][a_pos[1]] == 0:
                matrix[i][a_pos[1]] = -1
                p += 1
            elif matrix[i][a_pos[1]] == 6:
                break
    if a_down:
        for i in range(a_pos[0]+1, N):
            if matrix[i][a_pos[1]] == 0:
                matrix[i][a_pos[1]] = -1
                p += 1
            elif matrix[i][a_pos[1]] == 6:
                break
    if a_right:
        for i in range(a_pos[1]+1, M):
            if matrix[a_pos[0]][i] == 0:
                matrix[a_pos[0]][i] = -1
                p += 1
            elif matrix[a_pos[0]][i] == 6:
                break
    if a_left:
        for i in range(a_pos[1]-1, -1, -1):
            if matrix[a_pos[0]][i] == 0:
                matrix[a_pos[0]][i] = -1
                p += 1
            elif matrix[a_pos[0]][i] == 6:
                break
    return p

def count():
    invisible = 0
    for i in range(N):
        for k in range(M):
            if not matrix[i][k]:
                invisible += 1
    return invisible


cctv = []
direction = [0,
             [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)],
             [(1,1,0,0),(0,0,1,1)],
             [(1,0,1,0),(1,0,0,1),(0,1,1,0),(0,1,0,1)],
             [(1,1,1,0),(1,1,0,1),(1,0,1,1),(0,1,1,1)],
             [(1,1,1,1)]
             ]
matrix = []
N, M = map(int, sys.stdin.readline().strip().split())

for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().strip().split())))
for i in range(N):
    for k in range(M):
        if matrix[i][k] != 0 and matrix[i][k] != 6:
            cctv.append((i, k))

area = count()
invisible = [area]
if cctv:
    dfs(0)
print(invisible[0])
"""


def dfs(idx, s):
    global changed
    if idx == term:
        if len(s) > changed:
            changed = len(s)
    else:
        for watched_set in thing[idx]:
            dfs(idx + 1, watched_set | s)


def check(dir_list, x, y):
    s = set()
    for d in dir_list:
        di, dj = temp[d][0], temp[d][1]
        ni, nj = x + di, y + dj  # 중요
        while -1 < ni < n and -1 < nj < m:
            i, j = ni, nj
            if office[i][j] == 6:
                break
            elif office[i][j] == 0:
                s.add((i, j))
            ni, nj = i + di, j + dj
    return s


if __name__ == '__main__':
    n, m = map(int, input().split())
    office = [list(map(int, input().split())) for _ in range(n)]
    temp = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    types = [  # 상,하,좌,우 = 0, 1, 2, 3
        [],
        [[0], [1], [2], [3]],
        [[0, 1], [2, 3]],
        [[0, 2], [0, 3], [1, 2], [1, 3]],
        [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
        [[0, 1, 2, 3]],
    ]

    thing = []
    blind_spot = 0
    # min_val = n*m
    for i in range(n):
        for j in range(m):
            if office[i][j] == 0:
                blind_spot += 1
            elif office[i][j] != 6:
                thing.append([check(dirs, i, j) for dirs in types[office[i][j]]])
    changed = 0
    term = len(thing)
    # backtrack(0)
    dfs(0, set())
    # print(min_val)
    print(blind_spot - changed)



