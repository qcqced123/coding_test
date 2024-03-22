import sys


def solution():
    N = int(sys.stdin.readline())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    blue, white = [0], [0]

    def recursive(y: int, x: int, n: int):
        color = grid[y][x]
        for i in range(y, y+n):
            for j in range(x, x+n):
                if grid[i][j] != color:
                    recursive(y, x, n // 2)
                    recursive(y, x + (n // 2), n // 2)
                    recursive(y + (n // 2), x, n // 2)
                    recursive(y + (n // 2), x + (n // 2), n // 2)
                    return
        else:  # if loop is complete, then work flow come here
            if color == 1:
                blue[0] += 1
            else:
                white[0] += 1

    recursive(0, 0, N)
    print(white[0])
    print(blue[0])


if __name__ == "__main__":
    solution()
