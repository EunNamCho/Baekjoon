#하다가 pow함수 생각났는데
#pow는 인자를 3개 받는다
#첫번째는 밑, 두번째는 지수, 세번째는 그 계산한값의 나머지를 알고싶은 수
#즉, pow(100,2,3) == 100^2 % 3이다.


import sys


number = sys.stdin.readline().strip()
target = int(number)
length = len(number)
answer = list()
while True:
    num = list()
    num.append(int(number))
    for s in number:
        num.append(int(s))
    if target == sum(num):
        answer.append(num[0])
        number = int(number) - 1
        number = str(number)
    else:
        number = int(number) - 1
        number = str(number)
    if int(number) <= 1:
        break
if answer:
    print(min(answer))
else:
    print(0)