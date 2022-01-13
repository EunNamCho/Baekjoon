#DFS만 하니까 300ms정도 걸리는데
#그냥 connection검사 하니까 80ms
#웬만한 빠른 코드만큼 빨랐음
#위에가 DFS, 밑에가 connection


import sys

"""
def DFS(parent, start, desti):
    visited[start] = 1
    if vertex[start][desti]:
        vertex[parent][desti] = 1
        vertex[desti][parent] = 1
        exist.append(1)
    else:
        for idx in range(N):
            if vertex[start][idx] and not visited[idx]:
                vertex[parent][idx] = 1
                vertex[idx][parent] = 1
                DFS(parent, idx, desti)


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
visited = [0]*N
vertex = list()
flag, exist = False, []

for _ in range(N):
    vertex.append(list(map(int, sys.stdin.readline().strip().split())))

route = list(map(int, sys.stdin.readline().strip().split()))

for i in range(len(route)-1):
    start, desti = route[i]-1, route[i+1]-1
    if start == desti:
        exist.append(1)
    DFS(start, start, desti)
    if not exist:
        flag = True
        break
    visited, exist = [0] * N, []

if flag:
    print("NO")
else:
    print("YES")
"""


def d_DFS():
    num = 1
    for i in range(N):
        if not visited[i]:
            DFS(i, num)
            num += 1


def DFS(a_vertex, number):
    visited[a_vertex] = 1
    connect[a_vertex] = number
    for i in range(N):
        if vertex[a_vertex][i]:
            if not visited[i]:
                DFS(i, number)


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
visited = [0]*N
vertex = list()
connect = [0 for i in range(N)]
flag = False
for _ in range(N):
    vertex.append(list(map(int, sys.stdin.readline().strip().split())))

route = list(map(int, sys.stdin.readline().strip().split()))
d_DFS()
for i in range(len(route)-1):
    start, desti = route[i]-1, route[i+1]-1
    if connect[start] != connect[desti]:
        flag = True
        break
if flag:
    print("NO")
else:
    print("YES")
