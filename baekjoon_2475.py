import sys


answer = 0
number = list(map(int, sys.stdin.readline().strip().split()))
for elem in number:
    answer += pow(elem, 2)
print(answer % 10)