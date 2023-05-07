import sys
"""
[풀이 시간]
1) 17:00 ~ 17:30

[요약]
1) 동전의 종류가 주어질 때에 주어진 금액을 만드는 모든 방법을 세는 프로그램 작성
    - 주어지는 동전 단위를 가지고 목표 금액을 만들 수 있는 경우의 수를 모두 구하기
[전략]
1) 역시나 DP 문제
    - Table 어떻게 만들어야 할까
    - coin list를 내림차순 정렬, 가장 큰 수에서 하나씩 줄여 나가자
    - Knapsack처럼 푸는데 원소를 개수로 바꾼다.
"""
for _ in range(int(sys.stdin.readline())):
    N, coin_list, money = int(sys.stdin.readline()), list(map(int, sys.stdin.readline().split())), int(sys.stdin.readline())
    table = [[0] * money for _ in range(N+1)]

    for i in range(1, N+1):
        if table[0][i] % coin_list[0] == 0:
            table[0][i] = 1

    for row in range(1, N):
        for col in range(1, N+1):
            if col - coin_list[row] < 0:
                table[row][col] = table[row][col - 1]
            elif col % coin_list[row]




