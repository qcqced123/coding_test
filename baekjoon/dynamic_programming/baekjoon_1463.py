import sys

n = int(sys.stdin.readline())
dp = [0] * (n+1)

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1  # 안나눠지는 경우 때문에 무조건 앞에다가 빼놔야
    if i % 6 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1, dp[i // 2] + 1)

    elif i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

    elif i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

print(dp[-1])