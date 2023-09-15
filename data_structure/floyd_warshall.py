import sys
from typing import List
"""
[Floyd-Warshall]
1) DP Table init
2) triple-loop
    - dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
3) print result
"""


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
dp = [[float('inf')] * (N+1) for _ in range(N+1)]

# 1) DP Table init
for i in range(1, N+1):
    dp[i][i] = 0

for _ in range(M):
    src, end, cost = map(int, sys.stdin.readline().split())
    dp[src][end] = cost

# 2) triple-loop
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i == j:
                continue
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

# 3) print result
for i in range(1, N+1):
    for j in range(1, N+1):
        if dp[i][j] == float('inf'):
            print('INF', end=' ')
        else:
            print(dp[i][j], end=' ')
    print()
