import sys


def solution():
    """ 최대 수익, DP, NlogN
    한 번 시작, 그 상담 끝날 때 까지 다른 상담 불가

    T: 상담 필요 일수
    P: 금액

    idea: dynamic programming
        1) 날짜별 최대값 채우기
    """
    def is_valid() -> bool:
        return i+cnt_time < N + 2

    N = int(input())
    time, cost = [], []
    for _ in range(N):
        t, c = map(int, sys.stdin.readline().split())
        time.append(t), cost.append(c)

    cache = 0
    dp = [0]*(N+2)
    for i in range(1, N+1):
        cnt_time, cnt_cost = time[i-1], cost[i-1]
        cache = max(dp[i], cache)
        if is_valid():
            dp[i+cnt_time] = max(dp[i+cnt_time], cnt_cost+dp[i], cache+cnt_cost)

    print(max(dp))


if __name__ == "__main__":
    solution()
