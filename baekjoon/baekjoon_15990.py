import sys


def solution():
    """ 왜이리 어렵냐...
    idea: dynamic programming
        - 2d table
            - 행: 숫자
            - 열: 1,2,3 (어떤 경우의 수의 끝자리 숫자를 의미함)
    """
    # init the data structure
    input = sys.stdin.readline
    N = int(input())
    cache = [[0]*3 for _ in range(100001)]
    nums = [int(input()) for _ in range(N)]

    # update the dp cache
    cache[1], cache[2], cache[3] = [1, 0, 0], [0, 1, 0], [1, 1, 1]
    for i in range(4, 100001):
        cache[i][0] = (cache[i-1][1] + cache[i-1][2]) % 1000000009
        cache[i][1] = (cache[i-2][0] + cache[i-2][2]) % 1000000009
        cache[i][2] = (cache[i-3][0] + cache[i-3][1]) % 1000000009

    for t in nums:
        print(sum(cache[t]) % 1000000009)


if __name__ == "__main__":
    solution()
