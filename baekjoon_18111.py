import sys
from collections import defaultdict

n, m, b = map(int, sys.stdin.readline().strip().split())
matrix = []    # n x m
heights_counts = defaultdict(int)   # height : counts

for _ in range(n):
    row = list(map(int, sys.stdin.readline().strip().split()))
    for col in row:
        heights_counts[col] += 1
    matrix.append(row)

heights = list(heights_counts.keys())
counts = list(heights_counts.values())

min_costs = [99999999999999, 0] # cost, height

for i in range(len(heights)):
    standard = heights[i]
    costs = 0
    copy_b = b
    for j in range(len(heights)):
        if i != j:
            if standard < heights[j]:
                costs += counts[j] * 2
                copy_b += counts[j]
            elif standard > heights[j]:
                costs += counts[j] * 1
                copy_b -= counts[j]
                if copy_b < 0:
                    break
    if min_costs[0] > costs and copy_b >= 0:
        min_costs[0] = costs
        min_costs[1] = standard

print(min_costs[0], min_costs[1])