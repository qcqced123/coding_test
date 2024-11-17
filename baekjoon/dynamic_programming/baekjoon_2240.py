import sys


def solution():
    """
    idea: dynamic programming
        - 행: 초
        - 열: 이동횟수 (열방향에 제약조건을 세팅하자!)
    """
    input = sys.stdin.readline
    N, W = map(int, input().split())
    cache = [[0]*(W+2) for _ in range(N+1)]
    arr = [int(input()) for _ in range(N)]

    for i in range(1, N+1):
        cnt = arr[i-1]
        for j in range(1, W+2):
            curr = (j-1) % 2
            if (not curr and cnt == 1) or (curr and cnt == 2):
                cache[i][j] += 1
            cache[i][j] += max(cache[i-1][j - 1], cache[i - 1][j])

    print(max(cache[-1]))


if __name__ == "__main__":
    solution()
