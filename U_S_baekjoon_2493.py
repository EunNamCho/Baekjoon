#문제: 오큰수 풀듯이 풀었는데 시간초과가 뜸
#혹시나 pypy3로 컴파일 돌리니까 맞았습니다. 뜸.
#오큰수는 비교불가한 애들을 스택에 넣었는데
#이 문제는 큰 탑들을 스택에 집어넣음.
#print(' '.join(list(map(str, goto)))) list안써도됨.
#그리고 for문으로 출력하는것보다 join으로 출력하는게 더 빠름.
#미쳤따리 미쳤다....


import sys


size = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().strip().split()))
stack = list()
answer = [0 for _ in range(size)]
for i in range(1, size):
    if number[i] < number[i-1]:
        answer[i] = i
        stack.append(i-1)
    else:
        while stack:
            if number[stack[-1]] > number[i]:
                answer[i] = stack[-1] + 1
                break
            else:
                stack.pop()
for elem in answer:
    print(elem, end=' ')


n = int(sys.stdin.readline())
tower = list(map(int, sys.stdin.readline().strip().split()))
stack = list()
goto = [0] * n
for i in range(n):
    t = tower[i]
    while stack and tower[stack[-1]] < t:
        stack.pop()
    if stack:
        goto[i] = stack[-1] + 1
    stack.append(i)

print(' '.join(list(map(str, goto))))