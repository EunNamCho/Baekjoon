import sys


while True:
    palin = sys.stdin.readline().strip()
    if palin == '0':
        break
    flag = False
    for i in range(len(palin)//2):
        if palin[i] != palin[-(i+1)]:
            flag = True
            break
    if flag:
        print('no')
    else:
        print('yes')
