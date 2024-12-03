import sys
from bisect import bisect_left


def solution():
    """NlogN, 원형큐, 길이 M인 연속 부분 수열, upper bound
    idea:
        - 원형큐 처리
        - 1차원 배열의 부분합 구하기
        - 부분합 배열 정렬
        - 이분 탐색으로 현재 limit 값의 위치 찾기 (prefix 배열에서)
    """
    input = sys.stdin.readline
    for _ in range(int(input())):
        N, M, K = map(int, input().split())
        arr = list(map(int, input().split()))

        # make the circular queue
        circle = arr[:] + arr[:M]

        # init the prefix array with sliding window algorithm
        window = M
        init_ = sum(circle[:window])
        prefix = [init_]
        for i in range(1, N):
            init_ -= circle[i-1]
            init_ += circle[i+M-1]
            prefix.append(init_)

        # do sorting to prefix array and bisect
        prefix.sort()
        answer = bisect_left(prefix, K)
        if answer and N == M:
            answer = 1

        print(answer)


if __name__ == "__main__":
    solution()
