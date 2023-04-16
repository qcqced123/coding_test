import sys
""" Dynamic Programming: Knapsack Problem """

N, K = map(int, sys.stdin.readline().split())
item_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
item_list.sort(key=lambda x: x[0])
value_table = [[0 for _ in range(K+1)] for _ in range(N+1)]  # value_table: DP Table

for i in range(1, N+1):
    for j in range(1, K+1):
        weight, value = item_list[i-1]
        if weight > j:
            """ 현재 물건을 배낭에 담을 수 없는 경우 """
            value_table[i][j] = value_table[i-1][j]
        else:
            # 현재 물건을 배낭에 담을 수 있는 경우: 배열 인덱스 계산 유의, 특히 max() 첫번째 파라미터 인덱스 유의
            value_table[i][j] = max(value + value_table[i-1][j-weight], value_table[i-1][j])
print(value_table[-1][-1])

