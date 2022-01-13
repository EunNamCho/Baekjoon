import sys


def score(row, column):
    global m_score
    t_row1, t_column1 = row, column
    t_row2, t_column2 = row, column
    t_max = 0
    #가로
    while True:
        if 0 <= t_row1-1:
            t_row1 -= 1
            if board[t_row1][column] == 1:
                t_max += 1
        if t_row2+1 <= N-1:
            t_row2 += 1
            if board[t_row2][column] == 1:
                t_max += 1
        if 0 > t_row1-1 and t_row2+1 > N-1:
            m_score = max(t_max+1, m_score)
            t_row1, t_column1 = row, column
            t_row2, t_column2 = row, column
            t_max = 0
            break
    #세로
    while True:
        if 0 <= t_column1-1:
            t_column1 -= 1
            if board[row][t_column1] == 1:
                t_max += 1
        if t_column2+1 <= N-1:
            t_column2 += 1
            if board[row][t_column2] == 1:
                t_max += 1
        if 0 > t_column1-1 and t_column2+1 > N-1:
            m_score = max(t_max+1, m_score)
            t_row1, t_column1 = row, column
            t_row2, t_column2 = row, column
            t_max = 0
            break
    #왼쪽 대각
    while True:
        if 0 <= t_column1-1 and 0 <= t_row1-1:
            t_column1 -= 1
            t_row1 -= 1
            if board[t_row1][t_column1] == 1:
                t_max += 1
        if t_column2+1 <= N-1 and t_row2+1 <= N-1:
            t_column2 += 1
            t_row2 += 1
            if board[t_row2][t_column2] == 1:
                t_max += 1
        if (0 > t_column1-1 or 0 > t_row1-1) and \
                (t_column2+1 > N-1 or t_row2+1 > N-1):
            m_score = max(t_max+1, m_score)
            t_row1, t_column1 = row, column
            t_row2, t_column2 = row, column
            t_max = 0
            break
    #오른쪽 대각
    while True:
        if 0 <= t_column1-1 and 0 <= t_row2-1:
            t_column1 -= 1
            t_row2 -= 1
            if board[t_row2][t_column1] == 1:
                t_max += 1
        if t_column2+1 <= N-1 and t_row1+1 <= N-1:
            t_column2 += 1
            t_row1 += 1
            if board[t_row1][t_column2] == 1:
                t_max += 1
        if (0 > t_column1-1 or 0 > t_row2-1) and \
                (t_column2+1 > N-1 or t_row1+1 > N-1):
            m_score = max(t_max+1, m_score)
            t_row1, t_column1 = row, column
            t_row2, t_column2 = row, column
            t_max = 0
            break


N = int(sys.stdin.readline())
m_score = 0
white = []
board = []
for i in range(N):
    temp = list(map(int, sys.stdin.readline().strip().split()))
    board.append(temp)
    for j, elem in enumerate(temp):
        if elem == 2:
            white.append((i, j))
while white:
    pos = white.pop()
    score(pos[0], pos[1])
print(m_score)
