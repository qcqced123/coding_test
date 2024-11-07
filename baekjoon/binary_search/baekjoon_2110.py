import sys


def solution():
    """ 모든 집 커버, 최소 설치, NlogN,
    개별 경우의 수마다 거리의 최소값의 최대값
    idea: binary search
        - sorting
        - 탐색 대상: 거리값, range(1, max-min)
        - 포인터 이동 조건: 현재 거리 (S),
            -
        - 배열 선언 하지마 제발............

    """
    input = sys.stdin.readline
    N, C = map(int, input().split())
    house = [int(input()) for _ in range(N)]
    house.sort()

    answer = 0
    l, r = 0, house[-1]-house[0]  # 거리차가 1인 경우 떄문에, lower bound를 0으로 설정해야 제대로 탐색할 수 있다
    while l <= r:
        mid = (l+r) // 2
        prev, no_wifi = house[0], 0
        for home in house[1:]:
            if home - prev < mid: no_wifi += 1
            else: prev = home
            if N - no_wifi < C: break

        if N - no_wifi < C: r = mid - 1
        else:
            answer = mid
            l = mid + 1

    return answer


if __name__ == "__main__":
    print(solution())
