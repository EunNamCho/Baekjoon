# average optimal
import sys


n = int(sys.stdin.readline())
letters = sys.stdin.readline().strip()
M = 1234567891
r = 31
answer = 0
for idx, letter in enumerate(letters):
    answer += (ord(letter)-96)*(r**idx)
print(answer % M)
