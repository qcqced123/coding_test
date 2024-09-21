import sys
from typing import List


def solution():
    """ k개 연속된 접시 먹으면 할인, 앞에 할인 받으면 적힌 번호의 초밥 꽁짜 (없으면 새로 만듦)
    최대한 다양한 종류 초밥 먹기, 중복 초밥 있음, 원형 리스트 자료 구조(마지막 인덱스까지 탐색이 가능하게 만들면 됨)

    idea: two-pointer with sliding window (부분 수열에 중복된 숫자 최대한 줄이고, 쿠폰 번호 줄이고)
        1) 포인터 설정:
            - 포인터 위치: 윈도우 양쪽 끝
            - 포인터 방향: forward
            - 포인터 이동 조건: 없음, 동시 이동
            - 탐색 종료 조건: 왼쪽 포인터가 마지막에 닿으면 끝

        2) 초기 개수 세기
            => 초밥 가짓수 준 이유가 있구나
            => 사전을 미리 만들어서 개수로 판정해야 함
    """
    N, D, K, C = map(int, sys.stdin.readline().split())
    sushi = [int(input()) for _ in range(N)]*2

    # initialize dictionary for using cache
    # initialize the first kind value
    cache = {k: 0 for k in range(1, D+1)}
    cache[C] += 1
    for s in sushi[0:K]:
        cache[s] += 1

    # window sliding
    result = 0
    for v in cache.values():
        if v: result += 1

    for left in range(1, N):
        right = left + K - 1

        # check and update cache
        # remove old left value in cache, add the current new right value to cache
        cache[sushi[left-1]] -= 1
        cache[sushi[right]] += 1

        kind = 0
        for v in cache.values():
            if v: kind += 1

        result = max(result, kind)

    print(result)


if __name__ == "__main__":
    solution()
