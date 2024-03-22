import sys


def solution():
    sys.setrecursionlimit(10**4)
    N, r, c = map(int, sys.stdin.readline().split())

    def sol(l, y, x):
        if l == 0:
            return 0

        return 2 * (y % 2) + (x % 2) + 4 * sol(l-1, int(y / 2), int(x / 2))

    print(sol(N, r, c))


if __name__ == "__main__":
    solution()
