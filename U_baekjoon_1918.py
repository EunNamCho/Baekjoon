import sys


string = sys.stdin.readline().strip()
stack = list()
answer = ''
for s in string:
    if s == "+" or s == "-" or s == "*" or s == "/":
        stack.append(s)
    elif s == ")":
        if stack:
            answer += stack.pop()
    elif s == "(":
        pass
    else:
        answer += s
while stack:
    answer += stack.pop()
print(answer)
