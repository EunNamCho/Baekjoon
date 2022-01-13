#내 건 844ms
#진짜 빠른 사람껀 380~400ms 정도
#알고리즘은 거의 유사한데, 나는 매번 bomb과 같은지 확인했고
#그 사람은 스택에 집어넣은 글자가 bomb의 마지막과 일치하다면
#그 때 bomb과 같은지 확인함
#나도 그 생각했는데 ㄲㅂ...
#그리고 제일 중요한 핵심은 pop()이 아니라 del을 사용
#시간 차이가 엄청 발생

import sys

string = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()
answer = []
for char in string:
    answer.append(char)
    try:
        if ''.join(answer[-len(bomb):]) == bomb:
            del answer[-len(bomb):]
    except:
        pass
if not answer:
    print("FRULA")
else:
    print(''.join(answer))
