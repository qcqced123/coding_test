import sys


def solution():
    """ 부분 수열의 팰린드롬 여부 판정, N*M
    idea: DP
        1) 양 끝이 같고 중간 수열이 팰린드롬
    """
    N = int(input())
    arr = list(map(int, sys.stdin.readline().split()))
    dp = [[0]*N for _ in range(N)]

    # 1개 짜리 팰린드롬 처리
    for i in range(N):
        dp[i][i] = 1

    # 2개 짜리 팰린드롬 판정
    for j in range(1, N):
        if arr[j-1] == arr[j]:
            dp[j-1][j] = 1

    # 3개 이상 수열 팰린드롬 판정
    for r in range(2, N):
        for c in range(r, N):
            if arr[c-r] == arr[c] and dp[c-r+1][c-1]:
                dp[c-r][c] = 1

    # get answer
    M = int(input())
    for _ in range(M):
        src, end = map(int, sys.stdin.readline().split())
        print(dp[src-1][end-1])


if __name__ == "__main__":
    solution()
