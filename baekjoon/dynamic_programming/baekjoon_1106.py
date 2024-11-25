import sys


def solution():
    """ 투자 비용 최소값
    idea: dynamic programming
        - "정수배"
        - 제약 조건: 유치 고객
            - 행: 도시
            - 열: 유치 고객
            - 원소값: 비용
            - 초기값: ..? INF?
        - j 값에 딱 맞출 필요가 없구나... 그냥 넘겨도 되네 ......
    """
    # init the data structure
    INF = sys.maxsize
    input = sys.stdin.readline
    C, N = map(int, input().split())

    cache = [[INF]*(C+1) for _ in range(N+1)]
    arr = [tuple(map(int, input().split())) for _ in range(N)]
    arr.sort(key=lambda x: x[1])  # (비용, 사람수)

    # update the cache
    for i in range(1, N+1):
        cost, person = arr[i-1][0], arr[i-1][1]
        for j in range(1, C+1):
            y, x = divmod(j, person)
            if x: y += 1
            cache[i][j] = min(cache[i-1][j], cache[i][j], y*cost)
            for k in range(1, j//2+1):
                cache[i][j] = min(cache[i][j], cache[i][k] + cache[i][j-k])

    print(cache[-1][-1])


if __name__ == "__main__":
    solution()
