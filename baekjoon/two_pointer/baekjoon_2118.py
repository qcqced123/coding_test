import sys

INF = sys.maxsize
input = sys.stdin.readline


def solution():
    """
    idea: two pointer
        - 포인터 위치:
    """
    # get input data
    N = int(input())
    times = [int(input()) for _ in range(N)]
    arr = list(range(1, N+1))
    print(arr)

if __name__ == "__main__":
    solution()
