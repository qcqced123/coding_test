import sys


def solution():
    """
    idea: dynamic programming
    """
    # init data structure
    input = sys.stdin.readline
    N, S, M = map(int, input().split())
    arr = [0] + list(map(int, input().split()))
    cache = [[0]*(M+1) for _ in range(N+1)]
    cache[0][S] = 1

    for i in range(1, N+1):
        for j in range(M+1):
            if j + arr[i] <= M and cache[i-1][j+arr[i]]:
                cache[i][j] = 1

            if j - arr[i] >= 0 and cache[i-1][j-arr[i]]:
                cache[i][j] = 1
    answer = -1
    for i in range(M+1):
        if cache[-1][i] == 1:
            answer = i

    print(answer)


if __name__ == "__main__":
    solution()
