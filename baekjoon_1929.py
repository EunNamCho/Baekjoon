import sys
import math

M, N = map(int, sys.stdin.readline().split())
prime = [True] * (N+1)
prime[1] = False
answer = list()
for i in range(2, (N+1)):
    if prime[i]:
        for k in range(2, N//i+1):
            prime[k*i] = False
    if prime[i] and i >= M:
        answer.append(i)
print('\n'.join(map(str, answer)))


#이 코드가 왜 빠른가 생각해보기
"""
#Baekjoon_1929
import math

def eratosthenes(n):
  prime = [True]*(n+1)
  for i in range(2, math.floor(n ** 0.5)+1):
    if prime[i] == True:
      for j in range(2*i, n+1, i):
        prime[j] = False
  
  return [i for i in range(2,n+1) if prime[i] == True]

def lower_bound(arr, value):
  # sort된 배열 arr
  # arr 배열의 원소 중 조건을 만족하는 최솟값을 구함
  low, high = 0, len(arr)-1
  result = len(arr)-1

  while low <= high:
      mid = (low + high) // 2
      if value <= arr[mid]:
          high = mid - 1
          result = mid
          # 조건을 만족하는 경우 값을 result에 대입
      else:
          low = mid + 1
          
  return arr[result:len(arr)]

n, m = map(int, input().split())
primeL = lower_bound(eratosthenes(m), n)


print('\n'.join(map(str, primeL)))
"""
#이건테스트겸 그냥 짜본거
"""
M, N = map(int, sys.stdin.readline().split())
answer = list(range(M, N+1))
for elem in answer:
    flag = True
    for i in range(2, math.floor(elem ** 0.5)+1):
        if not(elem % i):
            flag = False
            break
    if flag:
        print(elem)

"""