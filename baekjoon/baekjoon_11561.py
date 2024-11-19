import sys


def solution():
    """
    idea: binary search
        - 탐색 대상/범위:
        - 탐색 조건:
    """
    # init
    input = sys.stdin.readline
    test = [int(input()) for _ in range(int(input()))]
    for t in test:
        answer = 0
        l, r = 1, t
        while l <= r:
            mid = (l+r) // 2

        print(answer)


if __name__ == "__main__":
    solution()
