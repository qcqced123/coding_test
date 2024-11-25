import sys


def solution():
    """ 순서 보존, 최소 그룹 개수, 블루레이 개수 == 그룹 개수, 블루레이 크기 최소화, 최대값의 최소화 문제
    idea: binary search
        - 최대값의 최소화 문제
        - 탐색 대상/범위: 블루레이 크기값 배열, 0 to sum(arr)
        - 탐색 기준: 현재 기준값을 최대로 만드는데 필요한 그룹의 개수
    point:
        1) 마지막 그룹 처리
        2) 단일 원소가 기준값 보다 클 떄 처리
    """
    # init the data structure
    input = sys.stdin.readline
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # do bisect
    answer = 0
    l, r = 1, sum(arr)
    while l <= r:
        mid = (l+r) // 2
        size, group = 0, 0
        for i, l in enumerate(arr):
            cnt = size + l
            if cnt <= mid:
                size += l
            else:
                group += 1
                size = l

            if i == N-1:
                group += 1

            if l > mid or group > M:
                break
        else:
            answer = mid
            r = mid - 1
            continue

        l = mid + 1

    print(answer)


if __name__ == "__main__":
    solution()
