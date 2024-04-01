import sys


def solution():
    sys.setrecursionlimit(10**4)
    N, r, c = map(int, sys.stdin.readline().split())

    def sol(l: int, y: int, x: int):
        if l == 0:
            return 0

        return 2 * (y % 2) + (x % 2) + 4 * sol(l-1, int(y / 2), int(x / 2))

    print(sol(N, r, c))


def solution2():
    result = 0
    N, r, c = map(int, sys.stdin.readline().split())
    while N:
        N -= 1  # split into half
        if r < 2**N and c < 2**N:  # 1사분면
            pass

        elif r < 2**N <= c:  # 2사분면
            result += (2**N)**2
            c -= 2**N

        elif r >= 2**N > c:
            result += 2 * (2**N)**2
            r -= 2**N

        else:
            result += 3 * (2**N)**2
            r -= 2**N
            c -= 2**N

    print(result)


def review_solution():
    result = 0
    N, r, c = map(int, sys.stdin.readline().split())
    while N:
        N -= 1
        if r < 2**N and c < 2**N:
            pass

        elif r < 2**N and c >= 2**N:
            result += (2**N)**2
            c -= 2**N

        elif r >= 2**N and c < 2**N:
            result += 2 * (2**N)**2
            r -= 2**N

        else:
            result += 3 * (2**N)**2
            r -= 2**N
            c -= 2**N
    print(result)


if __name__ == "__main__":
    solution()
