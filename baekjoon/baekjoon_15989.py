import sys


def solution():
    """
    idea: dynamic programming
        - dp[i] += dp[i-2] + dp[i-3]
    """
    N = int(input())
    cache = [1]*10001
    test = [int(input()) for _ in range(N)]

    # do the dynamic programming
    # case of adding the number "2"
    for i in range(2, 10001):
        cache[i] += cache[i-2]

    # case of adding the number "3"
    for i in range(3, 10001):
        cache[i] += cache[i-3]

    # answering the question
    for t in test:
        print(cache[t])


if __name__ == "__main__":
    solution()
