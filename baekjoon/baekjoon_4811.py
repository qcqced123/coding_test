import sys

INF = sys.maxsize
input = sys.stdin.readline


def sol_baekjoon_4811():
    """ solution func of baekjoon 15989
    idea: dynamic programming
        - 제약 조건: w 개수, h 개수
            - 행: w 개수 나열
            - 열: h 개수 나열
        - dp[i][j] = dp[i-1][j] + dp[i][j-1] (w추가 경우의 수 + h추가 경우의 수)
    """
    arr = []
    while True:
        t = int(input())
        if not t:
            break
        arr.append(t)

    cache = [[0] * 31 for _ in range(31)]

    # do update the dp cache
    cache[1][0], cache[1][1] = 1, 1
    for i in range(2, 31):
        for j in range(i + 1):
            cache[i][j] = cache[i - 1][j] + cache[i][j - 1]

    for i in arr:
        print(cache[i][i], end='\n')

    return


if __name__ == '__main__':
    sol_baekjoon_4811()
