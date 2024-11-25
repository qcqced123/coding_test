import sys


def solution():
    """ 구슬 배열 변경 불가(frozen), M개 그룹 나누기, 그룹의 숫자 합의 최대가 최소가 되도록 만들기
    idea: binary search
        - 탐색 기준: 그룹 개수(T)
            - T > M: l = mid + 1
            - T <= M: r = mid - 1, 정답 기록
        - 그룹 나누기
            - 기준값(mid)보다 커지면 그룹 개수 카운트
    feedback:
        - bisect를 사용하면, 그룹의 최대값의 최소값은 정확하게 구할 수 있지만, 기준 그룹 개수에 정확하게 맞지 않을 수도 있다
            - 그걸 저격한 문제구나
    좋은 반례:
    6 4
    1 1 1 4 1 1

    reference:
        https://www.acmicpc.net/board/view/52599
    """
    # init the data structure
    input = sys.stdin.readline
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # do bisect
    answer = 0
    answer_seq = []
    l, r = 1, sum(arr)
    while l <= r:
        cache = []
        mid = (l + r) // 2
        size, group, sub = 0, 0, []
        for i, l in enumerate(arr):
            cnt = size + l
            if cnt <= mid:
                size += l
                sub.append(l)

            else:
                group += 1
                size = l
                cache.append(sub)
                sub = [l]

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

    result = []
    seq_len = M - len(answer_seq)
    for seq in answer_seq:
        if seq_len:
            i = 0
            while seq_len and i < len(seq):
                result.append(1)
                seq_len -= 1
                i += 1

            if not seq_len:
                result.append(len(seq[i:]))

            continue

        result.append(len(seq))

    print(answer)
    print(*result)


def solution2():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # do bisect
    answer = 0
    l, r = 0, sum(arr)
    while l <= r:
        mid = (l+r) // 2
        cnt_group = 0
        idx = 0
        group = []
        while idx < N:
            sub_sum = 0
            sub_count = 0
            while idx < N and sub_sum + arr[idx]:
                pass



    return


if __name__ == "__main__":
    solution()
