import sys
import time


def recursive(x: int) -> int:
    if x < 2:
        return x
    return recursive(x - 1) + recursive(x - 2)


def memoization(x: int) -> int:
    if x < 2:
        return x

    if dp[x]:
        return dp[x]

    dp[x] = memoization(x - 1) + memoization(x - 2)  # 재귀 구조상 이미 계산한 값들을 다시 계산 하는 경우가 생기는데 그것을 방지
    return dp[x]


sys.setrecursionlimit(10**6)
start = time.time()
result = recursive(40)
end = time.time()

print(f"Execution Time: {end - start}")
print(f"Result: {result}")

n = 40
dp = [0] * (n + 1)

start = time.time()
result = memoization(n)
end = time.time()

print(f"Execution Time: {end - start}")
print(f"Result: {result}")
