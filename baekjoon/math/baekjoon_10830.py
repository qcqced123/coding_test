import sys


def solution():
    N, B = map(int, sys.stdin.readline().split())
    cache, matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)], []
    for c in range(N):
        tmp_row = []
        for r in range(N):
            tmp_row.append(cache[r][c])
        matrix.append(tmp_row)

    while B-1:
        for r in range(N):
            row = []
            for c in range(N):
                dot = 0
                for i, j in zip(cache[r], matrix[c]):
                    dot += i*j
                row.append(dot)
            cache[r] = row
        B -= 1

    for i in range(N):
        for j in range(N):
            cache[i][j] = cache[i][j] % 1000
        print(*cache[i], end='\n')


if __name__ == "__main__":
    solution()
