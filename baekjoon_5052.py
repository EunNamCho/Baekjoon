#노트에 길게 써놓음.


import sys
import heapq
r = sys.stdin.readline




test_case = int(sys.stdin.readline())
for _ in range(test_case):
    D = dict()
    H = []
    n = int(sys.stdin.readline())
    consistence = True
    for _ in range(n):
        heapq.heappush(H, sys.stdin.readline().strip())
    while H:
        number = heapq.heappop(H)
        if consistence:
            comparison = ''
            for char in number:
                comparison += char
                try:
                    if D[comparison]:
                        consistence = False
                        break
                except:
                    pass
        else:
            break
        D[number] = 1
    if consistence:
        print("YES")
    else:
        print("NO")



def solve(book):
    for p1, p2 in zip(book, book[1:]):
        print(p1,p2)
        if p2.startswith(p1):
            return False
    return True

T = int(r())
for _ in range(T):
    N = int(r())
    flag = True
    book = []
    for _ in range(N):
        book.append(r().strip())
    book.sort()
    print(book)
    if solve(book):
        print("YES")
    else:
        print("NO")
"""
1
4
89765
6516
565
897
"""