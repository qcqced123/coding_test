import sys
from bisect import bisect_left


def solution():
    """QlogN
    idea: binary search
        - 주어진 네모 배열이 오름 차순이 되도록, 그리드 반대로 생각하기
        - 방향별 연산 정의:
            - 위쪽 레이저: bisect 사용
            - 오른쪽 레이저: 인덱싱 사용
    """
    # get input
    input = sys.stdin.readline
    size, Q = map(int, input().split())
    arr = list(map(int, input().split()))
    queries = [tuple(map(int, input().split())) for _ in range(Q)]
    arr.reverse()

    # calculate
    for query in queries:
        answer = 0
        x, y = query
        ny = (size-1) - (y-1)
        nx = x - 1

        # add right raiser
        cnt = arr[ny]
        if nx < cnt:
            answer += arr[ny]-nx
            answer += ny - bisect_left(arr, x)

        print(answer)


if __name__ == "__main__":
    solution()
