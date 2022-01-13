import sys


target = list()
basket = list()
answer = list()
string = list()

for _ in range(int(sys.stdin.readline())):
    target.append(int(sys.stdin.readline()))

num = 1
t_max = max(target)
copy_target = target[:]

while True:
    if num > t_max + 1:
        break
    elif not(target):
        break
    elif num == target[0]:
        answer.append(num)
        num += 1
        string.append('+')
        string.append('-')
        del target[0]
    elif num < target[0]:
        string.append('+')
        basket.append(num)
        num += 1
    elif num > target[0]:
        if not(basket):
            break
        else:
            if basket[-1] == target[0]:
                answer.append(basket.pop())
                del target[0]
            else:
                del basket[-1]
        string.append('-')
if answer == copy_target:
    for s in string:
        print(s)
else:
    print("NO")