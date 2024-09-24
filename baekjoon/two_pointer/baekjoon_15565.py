import sys
from collections import Counter


def solution():
    """ 연속 인형 수열에 K개 이상의 라이언 인형 포함, 최소 집합의 크기

    idea: two pointer
        0) 초기값 설정
        1) 포인터 정보 초기화
            - 포인터 위치: 나란히
            - 포인터 이동 방향: forward
            - 포인터 이동 조건:
                - < K: right forward
                - >= K: left forward
    10 3 (인형 개수, 라이언 최소 필요 개수)
    1 2 2 2 1 2 1 2 2 1
              l
                      r
    10 2
    1 2 2 1 2 2 2 2 2 1
    l


    """
    N, K = map(int, sys.stdin.readline().split())
    dolls = list(map(int, sys.stdin.readline().split()))
    if K > Counter(dolls)[1]:
        print(-1)
        exit()

    l, r = 0, 0
    result = sys.maxsize
    cache = 1 if dolls[l] == 1 else 0
    while r < N:
        if cache < K:
            r += 1
            if r < N and dolls[r] == 1:
                cache += 1

        else:
            if cache == K:
                result = min(result, r - l + 1)

            if dolls[l] == 1:
                cache -= 1

            l += 1

    print(result)


if __name__ == "__main__":
    solution()
