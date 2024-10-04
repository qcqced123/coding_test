import sys


def solution():
    """ 125,000,000, (N^3)
    행렬 A: [n, m]
    행렬 B: [m, k]

    idea: dynamic programming
        1) 열 크기 증가, 비교 해야할 원소 개수도 같이 늘어남
    review:
        1) 이렇게 짜면, 중간의 시작점이 어딘지 모름
            - 예를 들어 인덱스 == 9의 원소를 최적화 할 때, 곱하기의 시작점이 4번, 5번, 6번 ... 8번 모두 경우의 수를
              비교해봐야 전역 최적을 구할 수 있음
            - 그래서 2차원 테이블이 필요함
    reference:
        https://ddiyeon.tistory.com/72

    """
    N = int(input())

    # initialize the row, col, cache array
    cache = [[0] * N for _ in range(N)]
    rows, cols = [], []
    for _ in range(N):
        row, col = map(int, sys.stdin.readline().split())
        rows.append(row), cols.append(col)

    # update the cache array
    for cnt in range(N-1):
        for i in range(N-1-cnt):
            j = cnt+i+1
            cache[i][j] = sys.maxsize
            for k in range(i, j):
                cache[i][j] = min(cache[i][j], cache[i][k] + cache[k+1][j] + rows[i] * cols[k] * cols[j])

    print(cache[0][-1])


if __name__ == "__main__":
    solution()
