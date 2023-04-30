import sys
"""
[풀이 시간]
1) 18:00 ~ 18:15

[요약]
1) 2원, 5원으로만 거슬러 줄 수 있음
    - '최소 동전 개수'로 거슬러 주는게 목표
    - 거슬러 줄 수 없으면 -1
[전략]
1) 2, 5, 7의 합으로 나타낼 수 없으면 거슬러 줄 수 없다
2) 동전 개수를 줄이는 것이 목표이기 때문에 최대한 5원으로 다 거슬러 주고 나머지를 2원으로 거슬러 준다
"""
M = int(sys.stdin.readline())
five_num = int(M / 5)
for i in range(five_num, -1, -1):
    checker = (M - (5 * i)) % 2
    if checker == 0:
        two_num = int((M - (5 * i)) / 2)
        print(i + two_num)
        exit()
    continue
print(-1)
