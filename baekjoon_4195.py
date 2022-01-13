import sys
from collections import defaultdict


def DFS(p_parent, p_person):
    visited[p_person] = True
    for person in D[p_person]:
        try:
            if visited[person]:
                pass
        except:
            D[p_parent].append(person)
            D[person].append(p_parent)
            DFS(p_person, person)


for _ in range(int(sys.stdin.readline())):
    L = []
    D = dict()
    idx = 0
    for _ in range(int(sys.stdin.readline())):
        a, b = input().split()
        try:
            if D[a]:
                pass
        except:
            L.append(idx)
            D[a] = idx
            idx += 1
        try:
            if D[b]:
                pass
        except:
            L.append(idx)
            D[b] = idx
            idx += 1
        if L[D[a]] != L[D[b]]:
            L[max(D[a], D[b])] = min(D[a], D[b])
