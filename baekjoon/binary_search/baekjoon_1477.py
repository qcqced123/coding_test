import sys


def solution():
    """ 거리, 휴게소 추가, 휴게소 없는 구간의 길이의 최댓값을 최소
    개별 경우의 수의 휴게소 없는 구간 길이 최대값들 중에서 최소값을 구하기

    [82, 201, 411, 555, 622, 755]

    0, 82, 201, 411, 555, 622, 755 800

    idea: binary search
        - 휴게소 배열 정렬
        - 탐색 대상/범위: 고속도로 길이, list(range(0, L+1))
        - 탐색 조건: "현재 거리"를 최대값으로 만드려면, 휴게소를 몇개 설치해야 하는가를 기준으로 돌리기
            -
    """
    input = sys.stdin.readline
    N, M, L = map(int, input().split())  # 휴게소 개수, 추가 휴게소 개수, 고속도로 길이
    rests = [0, L] + list(map(int, input().split()))  # 인덱스: 휴게소 개수, 원소값: 휴게소 위치
    rests.sort()

    answer = 0
    l, r = 0, L
    while l <= r:
        mid = (l+r) // 2
        prev, adds = 0, 0
        for rest in rests[1:]:
            cnt = rest - prev
            if cnt > mid:
                if mid:
                    i, j = divmod(cnt, mid)
                    if not j:
                        i -= 1
                    adds += i
                else:
                    adds += cnt

            prev = rest
            if adds > M:
                break

        if adds > M:
            l = mid + 1

        else:
            answer = mid
            r = mid - 1

    print(answer)


if __name__ == "__main__":
    solution()
