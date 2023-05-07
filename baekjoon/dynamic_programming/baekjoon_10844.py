import sys
"""
[풀이 시간]
1) 22:35 ~ 23:05

[요약]
1) 계단 수: 인접한 모든 자리의 차이가 1
    - 0으로 시작 X
    - 총 계단수가 몇개??
[전략]
1) Memorization 문제
    - 이 방법 내가 구현해본게 오래 되어 기억이 안난다 답지를 일단 보자
[Solution]
1) Make Table
    - Input N+1 Size for row, 10 size for column
    - 이전 레벨의 값을 그대로 가져 와서 더하기 때문에, 테이블 행을 저렇게 잡음
    - init value: 테이블 1행은 어차피 항상 고정, 미리 값을 초기화, 시작은 무조건 0이 아니기 때문에 0 빼고 나머지는 1로 초기화
2) Calculate Value
    - 자리수 2 이상 계산
    - 마지막 자리의 숫자가 0 또는 9인 경우만 1, 나머지는 2
    - 저런식으로 행마다 구해서 더하기
"""
N = int(sys.stdin.readline())
table, result = [[0]*10 for _ in range(N+1)], 0

for i in range(1, 10):
    table[1][i] = 1

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            table[i][j] = table[i-1][1]
        elif j == 9:
            table[i][j] = table[i-1][8]
        else:
            table[i][j] = table[i-1][j-1] + table[i-1][j+1]
for i in range(10):
    result += table[N][i]
print(result % 1000000000)
