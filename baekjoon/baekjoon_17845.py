import sys


def solution():
    """
    idea: dynamic programming
        - structure: 2d table
        - dp[i][j]: i번째 과목까지 고려했을 때, j시간 공부해서 얻을 수 있는 과목의 최대 중요도
    """
    # get input
    input = sys.stdin.readline
    N, K = map(int, input().split())
    candidate = [(0,0)] + [tuple(map(int, input().split())) for _ in range(K)]

    # update the dp cache for answering the question
    dp = [[0]*(N+1) for _ in range(K+1)]
    for i in range(1, K+1):
        importance, time = candidate[i]
        for j in range(1, N+1):
            prev = dp[i-1][j]
            if prev:
                dp[i][j] = prev
                if j + time <= N:
                    dp[i][j+time] = max(dp[i][j+time], prev+importance)

            if j == time:
                dp[i][j] = max(dp[i][j], importance)
    answer = 0
    for i in range(1, K+1):
        for j in range(1, N+1):
            answer = max(answer, dp[i][j])
    print(answer)


if __name__ == "__main__":
    solution()
