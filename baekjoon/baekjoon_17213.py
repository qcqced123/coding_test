import sys

INF = sys.maxsize
input = sys.stdin.readline


def solution():
    """
    idea: dynamic programming
        - 훔칠 수 있는 경우의 숫자 세기
        - dp[i][j]: i번 과일까지 고려했을 때, j개 훔친 모든 경우의 숫자
    """
    # get input data, init dp cache
    N = int(input())  # 과일 종류
    M = int(input())  # 훔칠 개수
    dp = [[0]*(M+1) for _ in range(N+1)]

    # do dynamic programming
    for i in range(1, N+1):
        for j in range(1, M+1):
            pass

    print(dp[-1][-1])


if __name__ == "__main__":
    solution()
