import sys

sys.setrecursionlimit(10**6)

def count_people(k, n):
    if apartment[k][n-1] == 0:
        apartment[k][n-1] = count_people(k-1, n) + count_people(k, n-1)
        return apartment[k][n-1]
    else:
        return apartment[k][n-1]

apartment = [[i for i in range(1,15)]]
for i in range(14):
    apartment.append([1]+[0]*13)

for _ in range(int(sys.stdin.readline())):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    count_people(k, n)
    print(apartment[k][n-1])
            
                
            

"""
(k, n): sum()

2: 1 4 10 20
1: 1 3 6 10 ... n(n+1)//2 ...
0: 1 2 3 4 ... n ...
"""