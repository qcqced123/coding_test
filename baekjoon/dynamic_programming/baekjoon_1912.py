import sys
"""
[풀이 시간]
1) 12:50 ~ 13:20

[요약]
1) n개의 정수로 이루어진 임의의 수열
    - 연속된 몇 개의 수를 선택 해서 구할 수 있는 합 중 가장 큰 합 구하기
    - 한 개 이상 무조건 선택
    - 10, -4, 3, 1, 5, 6, -35, 12, 21, -1 => 12+21 = 33
[전략]
1) 하위 수열 여러 개의 추이를 관찰
    - DP
    - 테이블 구조 & 점화식
    - 답지를 보자...
"""
N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
move = []
for i in range(N):
    if i == 0:
        move.append(num_list[0])
        continue
    move.append(max(move[i-1] + num_list[i], num_list[i]))
print(max(move))


