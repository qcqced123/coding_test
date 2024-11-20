import sys


def solution():
    """ 남은 시간 적절히 투자해, 최대 점수
    idea: dynamic programming
        - 제약 조건: 남은 시간
            - 행: 과목..?
            - 열: 남은 시간 나열
            - 원소: 현재 점수
    """
    # init the data structure
    input = sys.stdin.readline
    N, T = map(int, input().split())
    cache = [[0] * (T + 1) for _ in range(N+1)]
    arr = [tuple(map(int, input().split())) for _ in range(N)]

    # update the dp cache
    for i in range(1, N+1):
        cnt_cost, cnt_score = arr[i-1]
        if cnt_cost <= T:
            cache[i][cnt_cost] = max(cache[i-1][cnt_cost], cnt_score)

        for j in range(T+1):
            cache[i][j] = max(cache[i-1][j], cache[i][j])
            if cache[i-1][j] and j+cnt_cost <= T:
                cache[i][j+cnt_cost] = max(cache[i-1][j]+cnt_score, cache[i][j+cnt_cost])

    print(max(cache[-1]))


if __name__ == "__main__":
    solution()
