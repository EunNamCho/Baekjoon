#반례 A*((B*C)*D)*E, A+B*C*((D-E)*G)


import sys
from collections import deque


string = sys.stdin.readline().strip()
answer, sign, bracket = list(), deque(), deque()
flag = False
for char in string:
    if char.isalpha():
        answer.append(char)
        """
        if sign:
            if type(sign[-1]) == list:
                if sign[-1]:
                    if sign[-1][-1] == "*" or sign[-1][-1] == "/":
                        while sign[-1]:
                            answer.append(sign[-1].pop())
            else:
                if sign[-1] == "*" or sign[-1] == "/":
                    while sign:
                        answer.append(sign.pop())
                        """
        if sign:
            if type(sign[-1]) == list:
                if sign[-1]:
                    if sign[-1][-1] == "*" or sign[-1][-1] == "/":
                        answer.append(sign[-1].pop())
            else:
                if sign[-1] == "*" or sign[-1] == "/":
                    answer.append(sign.pop())
    else:
        if char == "(":
            if sign:
                if type(sign[-1]) != list:
                    bracket.append(sign.pop())
                    """
                    while sign:
                        answer.append(sign.pop())
                        """

                else:
                    bracket.append([])
            sign.append([])
        elif char == ")":
            while sign[-1]:
                answer.append(sign[-1].pop())
            sign.pop()
            if bracket:
                if type(bracket[-1]) != list:
                    answer.append(bracket.pop())
                else:
                    bracket.pop()
        else:
            if sign:
                if type(sign[-1]) == list:
                    if sign[-1]:
                        if sign[-1][-1] == "+" or sign[-1][-1] == "-":
                            if char == "+" or char == "-":
                                answer.append(sign[-1].pop())
                    sign[-1].append(char)
                else:
                    if sign[-1] == "+" or sign[-1] == "-":
                        if char == "+" or char == "-":
                            answer.append(sign.pop())
                    sign.append(char)
            else:
                sign.append(char)
while sign:
    answer.append(sign.pop())
print(''.join(answer))



#다른 사람 코드
#알고리즘은 똑같은데, 구현방법이 훨씬 간단함.
strn = list(input())
stack = []
res = ''
for s in strn:
    if s.isalpha():
        res += s
    else:
        if s == "(":
            stack.append(s)
        elif s == "*" or s == "/":
            while stack and (stack[-1] == "*" or stack[-1] == "/"):
                res += stack.pop()
            stack.append(s)
        elif s == "+" or s == "-":
            while stack and stack[-1] != "(":
                res+= stack.pop()
            stack.append(s)
        elif s == ")":
            while stack and stack[-1] != "(":
                res+=stack.pop()
            stack.pop()
while stack:
    res += stack.pop()
print(res)
