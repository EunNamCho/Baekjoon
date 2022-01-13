#그냥 list.sort이용
#python의 sort는 tim-sort를 이용
#tim-sort는 merge-sort와 insert-sort를 합친것
import sys
from collections import defaultdict
test_case = int(sys.stdin.readline())
data = []
for _ in range(test_case):
    data.append(int(sys.stdin.readline()))
data.sort()
mean = round(sum(data)/float(len(data)))
middle = data[int((len(data)-1)/2)]
counting = defaultdict(int)
for d in data:
    counting[d] += 1
freq = max(counting.values())
f_list = list()
for k, v in counting.items():
    if v == freq:
        f_list.append(k)
f_list.sort()
if len(f_list) >= 2:
    freq = f_list[1]
else:
    freq = f_list[0]
d_range = data[-1] - data[0]
print(mean)
print(middle)
print(freq)
print(d_range)