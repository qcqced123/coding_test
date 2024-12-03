import sys


def solution():
    """
    idea: binary search
        - 제약 조건:
            - 먹은 맥주 개수
            - 선호도의 합(M)
            - 이전에 받은 종류는 다시 못 받음

        - 탐색 대상/범위: 간 수치, 1 to max(arr)
        - 탐색 조건: mid라는 간 수치로 N개의 맥주를 먹고, M의 만족도를 달성했는가 못했는가 여부

        - 계산 알고리즘:
            - 그냥 루프 들어가기 전에, 선호도 기준으로 정렬하고, 선형 루프 돌리기
            - 이전에 받은 종류 못 받게 하려면, 선형 탐색 시키자
    """
    # init data structure
    input = sys.stdin.readline
    N, M, K = map(int, input().split())

    # do bisect with sorting
    answer = 0
    beer = []
    l, r = 1, 0
    for _ in range(K):
        v, c = map(int, input().split())
        beer.append((v, c))
        r = max(r, c)

    beer.sort(key=lambda x: -x[0])
    while l <= r:
        mid = (l+r) // 2
        cnt, nums = 0, 0
        for satis, limit in beer:
            if limit <= mid:
                cnt += satis
                nums += 1

            if nums == N and cnt >= M:
                break

        if nums == N and cnt >= M:
            answer = mid
            r = mid - 1
        else:
            l = mid + 1

    print(answer if answer else -1)


if __name__ == "__main__":
    solution()
