#핵심은 왼쪽으로 회전시킬지, 오른쪽으로 회전시킬지 결정하는거
#두 쪽 다 해보고 둘 중에 더 적게 회전하는 쪽을 반영함
#아 그리고 리스트(덱)복사를 좀 더 유의해야할듯


import sys, copy
from collections import deque


length, count = map(int, sys.stdin.readline().strip().split())
Deque = deque(range(1,length+1))
count = deque(map(int, sys.stdin.readline().strip().split()))
times = 0
while count:
  if Deque[0] == count[0]:
    Deque.popleft()
    count.popleft()
  else:
    right = 0
    left = 0
    r_temp = copy.deepcopy(Deque)
    l_temp = copy.deepcopy(Deque)
    while True:
      if r_temp[0] == count[0]:
        break
      else:
        r_temp.rotate(1)
        right += 1
    while True:
      if l_temp[0] == count[0]:
        break
      else:
        l_temp.rotate(-1)
        left += 1
    if right >= left:
      Deque = l_temp
      times += left
    else:
      Deque = r_temp
      times += right
print(times)