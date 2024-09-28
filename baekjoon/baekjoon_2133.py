import sys


def solution():
    """ 타일링 문제, 시간 복잡도 고려 X, 점화식 개까다로움

    idea: Dynamic Programming
        1) 점화식: f(n) = 3*f(n-2) + 2*sum(f[n-4] + f[n-6] + ...) + 2

    => 왜 x2를 안하고 했다고 생각한겨...?, 이렇게 오해 안했으면, 쉽게 이해했을텐데,,,,
    """
    N = int(input())
    if N == 1:
        print(0)
        exit()

    dp = [0]*(N+1)
    dp[2] = 3
    for i in range(3, N+1):
        if not i % 2:
            dp[i] = 3*dp[i-2] + 2
            for j in range(2, i-3, 2):
                dp[i] += 2*dp[j]

    print(dp[-1])


if __name__ == "__main__":
    solution()
