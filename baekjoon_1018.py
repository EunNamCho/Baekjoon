import sys


def count(color, row, column, pointer, ans):
    if not (pointer % 8):
        if color != Board[row][column]:
            ans += 1
    else:
        if color == Board[row][column]:
            ans += 1
    if pointer == 64:
        my_print()
        return ans
    else:
        origin.append(Board[row][column])
        modify.append(color)
        if not (pointer % 8):
            return count(Board[row][column], row+1, column-7, pointer+1, ans)
        else:
            return count(Board[row][column], row, column+1, pointer+1, ans)


def my_print():
    print('origin:')
    for idx, elem in enumerate(origin):
        print(elem, end='')
        if not((idx+1)%8):
            print()
    print('modify:')
    for idx, elem in enumerate(modify):
        print(elem, end='')
        if not((idx+1)%8):
            print()
    origin.clear()
    modify.clear()


N, M = map(int, sys.stdin.readline().strip().split())
Board = list()
answer = 100000000000000000
origin = list()
modify = list()
for i in range(N):
    Board.append(sys.stdin.readline().strip())
for i in range(N-8):
    for j in range(M-8):
        origin.append(Board[i][j])
        answer = min(answer, count('W', i, j+1, 1, 0))
        answer = min(answer, count('B', i, j+1, 1, 0))
print(answer)
