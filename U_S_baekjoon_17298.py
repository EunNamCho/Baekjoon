#인터넷 답보고 풀었음
#핵심은 전부 돌지 않고, 옆에꺼보다 크다면 스택에 담아놓고
#비교하는 것.


import sys

size = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().strip().split()))
stack = list()
answer = [-1 for _ in range(len(number))]
i = 0
while i < len(number)-1:
    if number[i] < number[i+1]:
        answer[i] = number[i+1]
        while stack:
            if number[stack[-1]] < number[i+1]:
                answer[stack.pop()] = number[i+1]
            else:
                break
    else:
        stack.append(i)
    i += 1
for elem in answer:
    print(elem, end=' ')


#문제: 탑 풀다가 새로운 방법보고 다시 짜보니 조금 더 빠름.
size = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().strip().split()))
stack = list()
answer = [-1 for _ in range(size)]
for i in range(size - 2, -1, -1):
    if number[i] < number[i + 1]:
        answer[i] = number[i + 1]
        stack.append(number[i + 1])
    else:
        while stack:
            if stack[-1] > number[i]:
                answer[i] = stack[-1]
                break
            else:
                stack.pop()
for elem in answer:
    print(elem, end=' ')