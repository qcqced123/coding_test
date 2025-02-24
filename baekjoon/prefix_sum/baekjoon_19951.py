import sys


def solution():
    """
    idea: prefix sum
    """
    # init data structure
    input = sys.stdin.readline
    N, M = map(int, input().split())  # nums of container, nums of teacher
    arr = list(map(int, input().split()))

    orders = [0] * (N + 1)
    for _ in range(M):
        a, b, k = map(int, input().split())
        orders[a - 1] += k
        orders[b] -= k

    cnt = 0
    for i in range(N):
        cnt += orders[i]
        print(arr[i] + cnt, end=" ")


if __name__ == "__main__":
    solution()
