import sys
"""
[풀이 시간]
1) 16:00 ~ 16:30

[요약]
1) 오르막 수: 수의 자리가 오름차순을 이루는 수
    - 오르막 수: 2234, 3678
    - 오르막 수 아닌거: 2232, 3676, 91111
    - 수의 길이 N이 주어 졌을 때, 오르막 수의 개수
[전략]
1) 이전 연산 정보가 필요한 DP 문제
"""
N, result = int(sys.stdin.readline()), 0
table = [[0] * 10 for _ in range(N+1)]

for i in range(10):
    table[1][i] = 1

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            table[i][j] = sum(table[i-1])
        elif j == 9:
            table[i][j] = 1
        else:
            table[i][j] = sum(table[i-1][j:])
result = sum(table[N])
print(result % 10007)
