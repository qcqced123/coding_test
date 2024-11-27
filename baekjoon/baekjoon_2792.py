import sys


def solution():
    """ 질투심으로 귀납적으로 찍고, 조건에 맞는지 확인
    idea: binary search
        - 탐색 대상/범위:
            - 최소 질투심(~학생 하나가 받을 수 있는 보석의 개수를 최소화)

        - 탐색 조건: 기준값(mid)를 만족하면서 모든 제약 조건을 만족 가능한가??
            - 가능: r = mid - 1, 정답 기록
            - 불가능: l = mid + 1
    """
    # get the input
    input = sys.stdin.readline
    N, M = map(int, input().split())
    jews = [int(input()) for _ in range(M)]  # array of jew

    # do binary search
    answer = 0
    l, r = sum(jews) // N, max(jews)
    while l <= r:
        mid = (l+r) // 2
        cnt = 0
        for jew in jews:
            divisor, remain = divmod(jew, mid)
            cnt += divisor
            if remain:
                cnt += 1

            if cnt > N:
                break

        if cnt > N:
            l = mid + 1

        else:
            answer = mid
            r = mid - 1

    print(answer)


if __name__ == "__main__":
    solution()
