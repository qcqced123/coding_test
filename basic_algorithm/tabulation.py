import sys
import time


def tabulation(x: int) -> int:
    """ Dynamic Programming Study
    1) Tabulation (Bottom-Up)
    """
    dp = [0] * (x + 1)
    dp[0], dp[1] = 0, 1
    for i in range(2, x + 1):
        dp[i] = dp[i - 2] + dp[i - 1]

    return dp[x]


start = time.time()
result = tabulation(40)
end = time.time()

print(f"Execution Time: {end - start}")
print(f"Result: {result}")