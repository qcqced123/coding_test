import sys


def solution():
    """
    idea: prefix sum
        - 2차원 테이블 누적합 문제
        - 정사각형 사이즈 경우의 수만큼 루프 돌려서, 최대값 갱신
    """
    INF = sys.maxsize
    input = sys.stdin.readline
    N = int(input())
    prefix = [[0]*(N+1) for _ in range(N+1)]
    grid = [list(map(int, input().split())) for _ in range(N)]

    # init prefix table
    for i in range(1, N+1):
        for j in range(1, N+1):
            prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + grid[i-1][j-1]

    # find the optimal solution
    answer = -INF
    for k in range(1, N+1):
        for i in range(N):
            for j in range(N):
                y1, x1 = i, j
                y2, x2 = i+k-1, j+k-1
                if -1 < y2 < N and -1 < x2 < N:
                    answer = max(answer, prefix[y2+1][x2+1]-prefix[y1][x2+1] - prefix[y2+1][x1] + prefix[y1][x1])
    print(answer)


if __name__ == "__main__":
    solution()
