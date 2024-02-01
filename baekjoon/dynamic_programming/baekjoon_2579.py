import sys


n = int(sys.stdin.readline())
stair = [0] + [int(sys.stdin.readline()) for _ in range(n)]

if n == 1 or n == 2:
    print(sum(stair))
    exit()

dp = [0] * (n+1)

dp[1] = stair[1]
dp[2] = stair[1] + stair[2]

for i in range(3, n+1):
    dp[i] = max(dp[i-2]+stair[i], dp[i-3]+stair[i-1]+stair[i])
print(dp[n])
