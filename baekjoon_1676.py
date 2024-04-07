import sys

#sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline().strip())
numbers = [i for i in range(1, n+1)]
two_fives = [0,0]

for number in numbers:
    while True:
        if number % 2 == 0:
            number = number // 2
            two_fives[0] += 1
        if number % 5 == 0:
            number = number // 5
            two_fives[1] += 1
        else:
            break
    
print(min(two_fives[0], two_fives[1]))

"""
2*5
3*3
2*2*2
7
2*3
5
2*2
3
2
1
"""