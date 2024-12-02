import sys


def solution():
    """
    idea: binary search
        - 탐색 대상/범위: 최소 몇판 더해야 하는지 판수, 0 to 1,000,000,000
        - 탐색 조건: 바뀌면 mid 값 줄이고, 안 바뀌면 늘리고
    """
    # init data structure
    INF = sys.maxsize
    input = sys.stdin.readline
    Y, X = map(int, input().split())
    Z = int(X * 100 / Y)

    # do bisect
    answer = 0
    l, r = 1, 1000000000
    while l <= r:
        mid = (l+r) // 2
        nz = int((X+mid)*100 / (Y+mid))
        if nz > Z:
            answer = mid
            r = mid - 1
        else:
            l = mid + 1

    print(answer if answer else -1)


if __name__ == "__main__":
    solution()
