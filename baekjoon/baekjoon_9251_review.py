import sys


def solution():
    """ LCS: 주어진 두 문자열에서 공통된 가장 긴 부분 수열 찾기

    idea: Dynamic Programming
        1) 같을 떄
            - 대각선 + 1
        2) 다를 때
            - max(왼쪽, 위쪽)
    """
    seq_a = "_" + sys.stdin.readline().rstrip()
    seq_b = "_" + sys.stdin.readline().rstrip()

    grid = [[0]*len(seq_a) for _ in range(len(seq_b))]
    for r in range(1, len(seq_b)):
        for c in range(1, len(seq_a)):
            if seq_b[r] == seq_a[c]:
                grid[r][c] = grid[r-1][c-1] + 1
                continue

            grid[r][c] = max(grid[r-1][c], grid[r][c-1])

    print(grid[-1][-1])

    return


if __name__ == "__main__":
    solution()
