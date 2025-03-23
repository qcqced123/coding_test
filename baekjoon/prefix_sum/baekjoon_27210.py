import sys

INF = sys.maxsize
input = sys.stdin.readline


def solution():
    """
    idea: prefix sum
    """
    # get input data
    N = int(input())
    arr = list(map(int, input().split()))

    # do prefix sum
    curr = 0
    answer = 0
    lower, upper = 0, 0
    for element in arr:
        if element == 1:
            curr += 1
        else:
            curr -= 1

        answer = max(answer, abs())


if __name__ == "__main__":
    solution()
