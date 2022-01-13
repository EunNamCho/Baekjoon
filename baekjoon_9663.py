import sys
import copy

N = int(sys.stdin.readline())
chess = []
answer, queen = 0, 0
for i in range(N):
    temp = [0] * N
    chess.append(temp)
for i in range(N):
    flag = True
    for k in range(N):
        if not chess[i][k]:
            temp = copy.deepcopy(chess)
            chess[i][k] = 10
            for j in range(N):
                if chess[i][j] != 10:
                    chess[i][j] = 1
                else:
                    chess = temp
                    flag = False
        if not flag:
            break
    if flag:
        queen += 1
        answer += 1
    if queen == N:
        break
print(answer)
