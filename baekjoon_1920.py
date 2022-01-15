"""
DICT로 푸는데 중복을 해결 못해서 못 품.
근데 생각해보니까 그냥 출력하거나 list에 넣으면 되는데...
그걸 생각을 못해서... 하...
"""

import sys


N = int(sys.stdin.readline())
N_arr = list(map(int, sys.stdin.readline().split()))
N_arr.sort()

M = int(sys.stdin.readline())
M_arr = list(map(int, sys.stdin.readline().split()))
answer = ['0'] * M


for idx, elem in enumerate(M_arr):
    right = len(N_arr)-1
    left = 0
    while left <= right:
        mid = (left + right) // 2
        if N_arr[mid] == elem:
            answer[idx] = '1'
            break
        elif N_arr[mid] > elem:
            right = mid - 1
        else:
            left = mid + 1
print('\n'.join(answer))
