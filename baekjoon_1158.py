import sys


my_input = sys.stdin.readline().strip().split()
Array = list(range(1, int(my_input[0])+1))
interval = int(my_input[1])
answer = list()
idx = 0
while Array:
    add = 1
    while add < interval:
        idx = (idx + 1) % len(Array)
        add += 1
    answer.append(Array.pop(idx))
answer = list(str(i) for i in answer)
print("<" + ', '.join(answer) + ">")