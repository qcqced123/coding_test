import sys

INF = sys.maxsize
input = sys.stdin.readline


def solution():
    """
    idea: prefix sum + dynamic programming
        - dp[i]: i일에 새롭게 태어난 벌레 숫자
    """
    a, b, d, N = map(int, input().split())
    dp = [0]*(N+1)
    dp[0] = 1

    prefix = 0
    for i in range(1, N+1):
        prefix = (prefix + dp[i-a] - dp[i-b] + 1000) % 1000
        dp[i] = prefix

    answer = 0
    for i in range(max(0, N-d+1), N+1):
        answer = (answer + dp[i]) % 1000

    print(answer)


if __name__ == "__main__":
    solution()
