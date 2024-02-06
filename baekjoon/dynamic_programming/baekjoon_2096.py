import sys


N = int(sys.stdin.readline())
max_dp, min_dp = [0, 0, 0], [0, 0, 0]

for _ in range(N):
    grid = tuple(map(int, sys.stdin.readline().split()))
    max_dp[0], max_dp[1], max_dp[2] = max(max_dp[0:2]) + grid[0], max(max_dp) + grid[1], max(max_dp[1:]) + grid[2]
    min_dp[0], min_dp[1], min_dp[2] = min(min_dp[0:2]) + grid[0], min(min_dp) + grid[1], min(min_dp[1:]) + grid[2]

print(max(max_dp), end=' ')
print(min(min_dp))
