# Quick
import sys


N = int(sys.stdin.readline())
answer = 0
numbers = list(map(int, sys.stdin.readline().split()))
prime = [True] * (max(numbers)+1)
prime[1] = False
for i in range(2, (max(numbers)+1)):
    if prime[i]:
        for k in range(2, max(numbers)//i+1):
            prime[k*i] = False
for number in numbers:
    if prime[number]:
        answer += 1

print(answer)
