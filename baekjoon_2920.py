import sys


answer = list(map(int, sys.stdin.readline().strip().split()))
flag = True
if answer[0] == 1:
    for i in range(7):
        if answer[i] != answer[i+1] - 1:
            flag = False
            break
    if flag:
        print("ascending")
    else:
        print("mixed")
elif answer[0] == 8:
    for i in range(7):
        if answer[i] != answer[i+1] + 1:
            flag = False
            break
    if flag:
        print("descending")
    else:
        print("mixed")
else:
    print("mixed")