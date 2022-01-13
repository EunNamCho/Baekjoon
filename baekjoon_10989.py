#메모리 초과가 뜸
#입력받는 수의 범위는 1~10000인데
#나는 배열을 test_case만큼 할당받아서 메모리 초과가 뜸
#그리고 input()으로 입력받으면 메모리 초과 뜰 수도 있다함

#counting-sort

import sys

sorting = [0 for _ in range(10001)]
for _ in range(int(sys.stdin.readline())):
    sorting[int(sys.stdin.readline())] += 1
for i in range(len(sorting)):
    if sorting[i] != 0:
        for k in range(sorting[i]):
            print(i)