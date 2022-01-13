#핵심은 reverse=False한거
#근데 나는 그후로 어떻게 해야할지 생각을 못했음.
#거의 도달했는데 짜증...


import sys, copy
from collections import deque


test_case = int(sys.stdin.readline())
for _ in range(test_case):
    func = sys.stdin.readline().strip()
    length = int(sys.stdin.readline())
    string = sys.stdin.readline().strip()
    string = deque(string[1:-1].split(','))
    reverse = False
    if not length:
        string.clear()
    try:
        for operation in func:
            if operation == "R":
                reverse = not reverse
            elif operation == "D":
                if reverse:
                    string.pop()
                else:
                    string.popleft()
    except:
        print("error")
        continue
    if reverse:
        string.reverse()
    print("[" + ",".join(string) + "]")