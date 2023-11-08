import sys
"""
[조건]
1) 1 ~ N개의 집이 순서
    - 이웃 끼리는 서로 다른 색상 (+ 가장자리끼리도 이웃처리)
[풀이]
1) 1번집의 색상을 고정, 3가지 경우의 수끼리 비교
    - 나머지 집은 그대로 이전 집 색상만 고려
        - 1번집의 색상을 무한대 처리, 나머지 색상 비용 중에서 최소값 도출
        - 이전 최소값과 비교, 최소값 업데이트 (모델 체크포인트 저장할 떄와 같은 로직)
"""


def solution():
    ans = float('inf')
    for k in range(3):
        dp = [[-1]*3 for _ in range(N+1)]
        dp[1] = [float('inf')]*3
        dp[1][k] = cost[0][k]

        for i in range(2, N+1):
            dp[i][0] = cost[i-1][0] + min(dp[i-1][1], dp[i-1][2])
            dp[i][1] = cost[i-1][1] + min(dp[i-1][0], dp[i-1][2])
            dp[i][2] = cost[i-1][2] + min(dp[i-1][0], dp[i-1][1])
        dp[N][k] = float('inf')
        ans = min(ans, min(dp[-1]))
    print(ans)


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    cost = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    solution()
