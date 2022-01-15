import sys

for _ in range(int(sys.stdin.readline())):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    b = 1
    answer = 0
    if k == 1:
        answer = n*(n+1)//2
    if b == 1:
        answer = 1
    else:
        for i in range(k+1, 0, -1):
            answer += (i*b)
            b += 1
    print(answer)
