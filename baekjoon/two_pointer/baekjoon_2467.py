import sys


def solution():
    """ 산성 용액: 양수, 알칼리 용액: 음수, 혼합 용액: 두 용액의 합
    최대한 0에 가깝게 만들자 (abs), NlogN

    idea: two pointer
        1) 배열 정렬
        2) 포인터 초기화
            - 포인터 위치: 양끝
            - 포인터 방향: forward, backward
            - 포인터 이동 조건:
                - > 0: right pointer backward
                - < 0: left pointer forward
    """
    N = int(input())
    chemical = list(map(int, sys.stdin.readline().split()))
    chemical.sort()

    l, r = 0, N-1
    best, best_record = 1e+10, None
    while l < r:
        cnt = chemical[l] + chemical[r]
        if best > abs(cnt):
            best = abs(cnt)
            best_record = [chemical[l], chemical[r]]

        if cnt > 0:
            r -= 1

        else:
            l += 1

    for i in best_record:
        print(i, end=' ')


if __name__ == "__main__":
    solution()
