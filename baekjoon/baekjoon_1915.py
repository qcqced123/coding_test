import sys


def solution():
    """ 내부 모든 원소가 1인 정사각형, 최대값, 1,000,000 (N^2logN)
    idea: dynamic programming
        1) if grid[r][c]:
            왼쪽, 왼쪽 위 대각, 위쪽 모두 0보다 클 떄 기준
            1-1) 셋다 값이 같을 때:
                (값 + 1) ** 2
            1-2) 값이 하나라도 다를 때:
                (min(l, u, lu) + 1)**2

    """
    N, M = map(int, sys.stdin.readline().split())

    grid = []
    for _ in range(N):
        tmp = list(map(str, sys.stdin.readline().rstrip()))
        cnt = [int(t) for t in tmp]
        grid.append(cnt)

    dp = [[0]*M for _ in range(N)]

    cache = 0
    for y in range(N):
        for x in range(M):
            if not grid[y][x]:
                continue

            l, u, lu = dp[y][x-1], dp[y-1][x], dp[y-1][x-1]
            if l and u and lu:
                if l == u == lu:
                    dp[y][x] = int((pow(l, 1/2) + 1)**2)  # 데이터 타입을 정수형으로 바꿔줘야 통과

                else:
                    dp[y][x] = int((pow(min(l, u, lu), 1/2) + 1)**2)  # 데이터 타입을 정수형으로 바꿔줘야 통과
            else:
                dp[y][x] = grid[y][x]

            cache = max(cache, dp[y][x])

    print(cache)


if __name__ == "__main__":
    solution()
