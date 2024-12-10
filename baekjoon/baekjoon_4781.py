import sys


def solution():
    """
    idea: dynamic programming
        - structure: dp[i][j] = i번재 사탕까지 고려했을 때, j번째 금액을 만족하는 경우 중에서 가장 큰 칼로리 값
            - 제약 조건: 돈
            - 구조: 사탕들*돈
        - overlapping:
        - cache:
    """
    INF = sys.maxsize
    input = sys.stdin.readline
    while True:
        N, M = map(float, input().split())
        if not N and M == 0.00:
            break

        # init data structure and update dynamic programming
        N = int(N)
        M = int(M)
        dp = [[-INF] * (M + 1) for _ in range(N + 1)]
        data = [(0, 0)] + [tuple(map(float, input().split())) for _ in range(N)]
        for i in range(1, N+1):
            cnt_cal, cnt_cost = data[i]
            for j in range(1, M+1):
                d, r = divmod(j, cnt_cost)
                dp[i][j] += dp[i-1][j]
                if not r:
                    dp[i][j] = max(dp[i][j], d*cnt_cal)

                for k in range(1, int(d)+1):
                    dp[i][j] = max(dp[i][j], dp[i-1][j-int(cnt_cost*k)]+dp[i][int(cnt_cost*k)])

        print(int(dp[-1][-1]))


if __name__ == "__main__":
    solution()
