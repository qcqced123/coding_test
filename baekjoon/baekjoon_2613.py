import sys


def solution():
    """ 구슬 배열 변경 불가(frozen), M개 그룹 나누기, 그룹의 숫자 합의 최대가 최소가 되도록 만들기
    idea: binary search
        - 탐색 기준: 그룹 개수(T)
            - T > M: l = mid + 1
            - T <= M: r = mid - 1, 정답 기록
        - 그룹 나누기
            - 기준값(mid)보다 커지면 그룹 개수 카운트
    """
    # init the data structure
    input = sys.stdin.readline
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # do bisect
    answer = 0
    answer_seq = []
    l, r = 0, sum(arr)
    # do bisect
    answer = 0
    l, r = 1, sum(arr)
    while l <= r:
        cache = []
        mid = (l + r) // 2
        size, group, sub = 0, 0, 0
        for i, l in enumerate(arr):
            cnt = size + l
            if cnt <= mid:
                size += l
                sub += 1

            else:
                group += 1
                size = l
                cache.append(sub)
                sub = 1

            if i == N-1:
                group += 1
                cache.append(sub)

            if l > mid or group > M:
                break
        else:
            answer = mid
            answer_seq = cache
            r = mid - 1
            continue

        l = mid + 1

    print(answer)
    print(*answer_seq)


if __name__ == "__main__":
    solution()
