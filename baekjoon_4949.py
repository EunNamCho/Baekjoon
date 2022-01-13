#sys.stdin.readline()는 개행문자까지 입력받는다
#3을 받으면 3\n이다.


#스택 1개를 이용하면 됨.
#초반에 소괄호, 대괄호 리스트 따로따로 만들어서 틀림.


import sys


while True:
    sentence = sys.stdin.readline().rstrip()
    brackets = list()
    if sentence == ".":
        break
    for letter in sentence:
        if letter == "(" or letter == ")":
            if not(brackets):
                brackets.append(letter)
            else:
                if letter == ")" and brackets[-1] == "(":
                    brackets.pop()
                else:
                    brackets.append(letter)
        elif letter == "[" or letter == "]":
            if not(brackets):
                brackets.append(letter)
            else:
                if letter == "]" and brackets[-1] == "[":
                    brackets.pop()
                else:
                    brackets.append(letter)
    if not(brackets):
        print("yes")
    else:
        print("no")