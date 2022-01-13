import sys
"""틀린코드
def dfs(idx):
    if not visited.get(pos[idx]):
        visited[pos[idx]] = 1
        for i, elem in enumerate(pos):
            if matrix[idx][i] and not visited.get(pos[i]):
                if i == N+1:
                    return True
                return dfs(i)
"""
def dfs(idx):
    ret = False
    if not visited.get(pos[idx]):
        visited[pos[idx]] = 1
        for i, elem in enumerate(pos):
            if matrix[idx][i] and not visited.get(pos[i]):
                if i == N+1:
                    return True
                ret = dfs(i) or ret
        return ret



T = int(sys.stdin.readline())
for _ in range(T):
    visited = {} #방문한 좌표 저장
    pos = list() #출발좌표, 편의점좌표, 페스티벌 좌표 순서로 저장
    N = int(sys.stdin.readline()) #편의점 갯수
    matrix = [[0] * (N + 2) for _ in range(N + 2)] #(pos, pos)의 그래프
    pos.append(tuple(map(int, sys.stdin.readline().strip().split())))
    for _ in range(N):
        pos.append(tuple(map(int, sys.stdin.readline().strip().split())))
    pos.append(tuple(map(int, sys.stdin.readline().strip().split())))
    #각 좌표들끼리 거리가 1000이내라면 edge로 연결
    for i, pos1 in enumerate(pos):
        for k, pos2 in enumerate(pos):
            if abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1]) <= 1000 and i != k:
                matrix[i][k] = 1
    answer = dfs(0)
    if answer:
        print('happy')
    else:
        print('sad')
