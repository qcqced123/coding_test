import sys

INF = sys.maxsize
input = sys.stdin.readline


def solution():
    """
    idea: prefix sum
        -
    limit: NlogN
    """
    N, Q = map(int, input().split())
    cities = [list(map(int, input().split())) for _ in range(N)]  # population, position

    prefix = [0]*(int(2e+6)+1)
    print(*list(range(-14, 15)))




if __name__ == "__main__":
    solution()
