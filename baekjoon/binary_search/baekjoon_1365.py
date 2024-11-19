import sys
from bisect import bisect_left


def solution():
    """ 한 개씩 연결, 자르는 횟수 최소, "꼬인다" => 전선이 크로스, NlogN
    꼬인걸 해결 하려면, 왼쪽 노드 번호가 모두 동일한 기준에 의해 오른쪽 노드와 연결되어야 한다
        - 모두 자기 자신보다 크거나
        - 모두 자기 자신과 같거나
        - 모두 자기 자신보다 작거나
    idea: binary search
        - 노드 개수 - 가장 긴 증가하는 부분 수열
            - NlogN, dynamic programming 로 못구함
            -
    """
    # init the data structure
    input = sys.stdin.readline
    N = int(input())
    arr = list(map(int, input().split()))
    # find the longest ascending sub sequence in whole array
    frame = -1
    cache = []
    for i in range(N):
        cnt = arr[i]
        if cnt >= frame:
            cache.append(cnt)

        else:
            idx = bisect_left(cache, cnt)
            cache[idx] = cnt

        frame = cache[-1]

    print(N-len(cache))


if __name__ == "__main__":
    solution()
