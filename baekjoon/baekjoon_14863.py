import sys


def solution():
    """ 경로는 픽스, 시작 and 도착지 픽스, 시간 내 최대 모금액
    무조건 구간을 방문은 해야 하는데, 둘 중 하나를 꼭 반드시 선택하는 대신, 시간 제약을 만족하면서 최대 모금액을 구해라
    시간 많을 때는 걷고, 시간 없을 떄는 자전거 타고

    idea: dynamic programming
        - approach: top-down with cache (recursive 굳이 쓰지말고, 뒤집고, 루프로 접근 해도 될 것 같음
        - structure:
        - cache:
        -
    reference:
        - https://www.acmicpc.net/board/view/151137
        - https://www.acmicpc.net/board/view/54475

    => 근데, 어차피 현재 구간을 반드시 들러야 해서, 최대 시간만 안 넘으면, 계속 기록해주고, 끝내면 될 거 같은데??
    => bottom-up 접근하고, 완탐처럼 다 캐시에 기록하되, 가지만 잘 쳐주는 방식으로 풀릴것 같음
    """
    input = sys.stdin.readline
    N, K = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(N)]  # 도보 시간, 도보 금액, 자전거 시간, 자전거 금액

    # init dp cache
    # 첫 줄에 대한 dp 캐시 초기화 할 때, 자전거 & 걷는게 같은 시간이 걸릴 수도 있음...
    dp = [[0]*(K+1) for _ in range(N)]
    dp[0][info[0][0]] = max(dp[0][info[0][0]], info[0][1])
    dp[0][info[0][2]] = max(dp[0][info[0][2]], info[0][3])

    # update the dp cache
    for i in range(1, N):
        cnt = info[i]
        for j in range(K+1):
            if dp[i-1][j]:
                path1_cost = j + cnt[0]
                path2_cost = j + cnt[2]
                if path1_cost <= K:
                    dp[i][path1_cost] = max(dp[i][path1_cost], dp[i-1][j]+cnt[1])
                if path2_cost <= K:
                    dp[i][path2_cost] = max(dp[i][path2_cost], dp[i-1][j]+cnt[3])

    print(max(dp[-1]))


if __name__ == "__main__":
    solution()
