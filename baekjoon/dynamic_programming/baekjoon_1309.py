import sys


def solution():
    """ NlogN, 1D dp array
    idea: dynamic programming
        - 3*N짜리 dp 캐시 만들기
            - 하나도 안놓는 경우, 왼쪽에 두는 경우, 오른쪽에 두는 경우
            - dp[i][0] = sum(dp[i-1])
            - dp[i][1] = dp[i-1][0] + dp[i-1][2]
            - dp[i][2] = dp[i-1][0] + dp[i-1][1]
    """
    N = int(input())
    cache = [[0]*3 for _ in range(N)]

    cache[0][0], cache[0][1], cache[0][2] = 1, 1, 1
    for i in range(1, N):
        cache[i][0] = sum(cache[i-1]) % 9901
        cache[i][1] = (cache[i-1][0] + cache[i-1][2]) % 9901
        cache[i][2] = (cache[i-1][0] + cache[i-1][1]) % 9901

    print(sum(cache[N-1]) % 9901)


if __name__ == "__main__":
    solution()
