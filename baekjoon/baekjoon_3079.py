import sys


def solution():
    """ 사람 10억명, 심사대 10만, NlogN
    시간의 최소값을 구해야 하기 떄문에, 시간 배열을 대상으로 탐색하면 된다.

    idea: binary search
        - 탐색 대상/기준: 시간 배열
        - 탐색 기준: 현재 시간에서 처리 가능한 인원수 (T)
            if T < M: l forward
            elif T >= M: r backward

        - 시간값으로 처리 가능한 인원수 찾는 알고리즘
            - sum(시간 // 개별심사 걸리는 시간)
    """
    answer = sys.maxsize
    input = sys.stdin.readline
    N, M = map(int, input().split())  # 심사대, 사람 숫자
    judge = [int(input()) for _ in range(N)]
    judge.sort()

    l, r = 0, judge[0] * M
    while l <= r:
        mid = (l+r) // 2
        cache = 0
        for delay in judge:
            cache += mid // delay

        if cache < M:
            l = mid + 1

        else:
            answer = min(answer, mid)
            r = mid - 1

    print(answer)


if __name__ == "__main__":
    solution()
