import sys

def round (x):
    if int(x) > 0 and x % int(x) >= 0.5:
        return int(x) + 1
    return int(x)

n = int(sys.stdin.readline())
difficulties = []

for _ in range(n):
    difficulty = int(sys.stdin.readline())
    difficulties.append(difficulty)

difficulties.sort()
outlier = round(n * 0.15)

for _ in range(outlier):
    try:
        difficulties.pop()
        difficulties.pop(0)
    except:
        pass

mean = round(sum(difficulties) / len(difficulties)) if len(difficulties) > 0 else 0
print(mean)