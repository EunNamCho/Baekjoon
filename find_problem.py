import os

problem = input("찾고싶은 문제 번호: ")
dir = os.listdir()
dir = [file.split("_")[-1][:-3] for file in dir]
print(dir)
if problem in dir:
    print("있는 문제입니다.")
else:
    print("없는 문제입니다.")