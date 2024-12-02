import sys


def solution():
    """ O(R*C*Q)

    idea: prefix sum
        - 2D table prefix sum
        - prefix[i][j]: s
    """
    input = sys.stdin.readline
    R, C, Q = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(R)]
    queries = [tuple(map(int, input().split())) for _ in range(Q)]

    # init prefix 2d array
    prefix = [[0]*(C+1) for _ in range(R+1)]
    for i in range(1, R+1):
        for j in range(1, C+1):
            prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + grid[i-1][j-1]

    # answering the question
    # do minus one at each index position of query
    for query in queries:
        ly, lx, ry, rx = query
        nums = (ry+1-ly)*(rx-lx+1)
        target_sum = prefix[ry][rx] - prefix[ly-1][rx] - prefix[ry][lx-1] + prefix[ly-1][lx-1]
        print(target_sum // nums)


if __name__ == "__main__":
    solution()
