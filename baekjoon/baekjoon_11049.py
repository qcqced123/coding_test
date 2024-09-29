import sys


def solution():
    """ 125,000,000, (N^3)
    행렬 A: [n, m]
    행렬 B: [m, k]

    idea: dynamic programming
        1) dp[i] = min(dp[i-1] + arr[i-2]*arr[i], arr[i-1]*arr[i]*arr[i-2] + dp[i-2])
    """
    N = int(input())
    matrix = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]  # row, col

    # initialize the cache array
    cache = [0]*N
    if N > 1:
        y, x = matrix[0]
        _, z = matrix[1]
        cache[1] = y*x*z
    else:
        y, x = matrix[0]
        print(y*x)
        return

    for i in range(2, N):
        cnt_y, cnt_x = matrix[i]
        prev_y, prev_x = matrix[i-1]  # 인덱스 한 칸 이전
        past_y, past_x = matrix[i-2]  # 인덱스 두 칸 이전

        cache[i] = min(
            cache[i-1] + past_y*prev_x*cnt_x,
            cache[i-2] + prev_y*prev_x*cnt_x + past_y*past_x*cnt_x
        )

    print(cache[-1])


if __name__ == "__main__":
    solution()
