import sys

INF = sys.maxsize
input = sys.stdin.readline


def solution():
    """
    idea: prefix + dynamic programming
    """
    # get input data
    N, M = map(int, input().split())  # city, day
    arr = list(map(int, input().split()))
    metro = [list(map(int, input().split())) for _ in range(N-1)]

    print(arr)
    print(metro)



if __name__ == "__main__":
    solution()
