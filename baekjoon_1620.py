#str.isdescimal, str.isnumeric, str.isdigit
#데시말은 int함수로 변환이 가능하면 True
#넘머릭은 제곱, 루트 같은 특수기호도 숫자로 인정
#디지트는 숫자로 보이면 모두 True


import sys


size, test_case = map(int, sys.stdin.readline().strip().split())
D = dict()
L = list()
for i in range(size):
    name = sys.stdin.readline().strip()
    D[name] = i+1
    L.append(name)
for _ in range(test_case):
    ask = sys.stdin.readline().strip()
    try:
        print(L[int(ask) - 1])
    except:
        print(D[ask])