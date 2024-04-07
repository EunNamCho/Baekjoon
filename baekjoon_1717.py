#핵심은 path compression이 중요
#한 번 탐색하고 그 탐색하는 동안에 같은 뿌리라면
#바로 밑에 달아주는 작업


import sys
sys.setrecursionlimit(10**6)


def find_root(a):
    if disjoint[a] == a:
        while path:
            disjoint[path.pop()] = a
        return a
    else:
        path.append(a)
        return find_root(disjoint[a])


path = list()
size, test_case = map(int, sys.stdin.readline().strip().split())
disjoint = dict()
for i in range(size+1):
    disjoint[i] = i
for _ in range(test_case):
    action = list(map(int, sys.stdin.readline().strip().split()))
    if action[0]:
        if find_root(action[1]) == find_root(action[2]):
            print("YES")
        else:
            print("NO")
    else:
        f_root, s_root = find_root(action[1]), find_root(action[2])
        if f_root != s_root:
            disjoint[f_root] = s_root
