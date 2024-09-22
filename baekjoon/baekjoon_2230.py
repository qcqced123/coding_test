import sys


def solution():
    """ 두 수를 고르고, 차이가 M 이상, 차이가 M이랑 가장 가까운 경우, M이랑 가장 가까운 경우 출력, NlogN

    idea: two pointer
        1) 배열 오름차순 정렬
        2) 포인터 설정 초기화:
            - 포인터 위치: 양 끝
            - 포인터 방향: forward, backward
            - 포인터 이동 조건:
                - > current best >= M: left forward
                - current best > >= M: right forward
                - < M: right forward
    1, 2, 3, 4, 5
    l        r

    """
    N, M = map(int, sys.stdin.readline().split())
    arr = [int(input()) for _ in range(N)]
    arr.sort()

    best = sys.maxsize
    l, r = 0, 1
    while l < r < N:
        cnt = abs(arr[l] - arr[r])
        if cnt < M:
            r += 1

        else:
            if cnt > best:
                l += 1
            else:
                best = cnt
                r += 1

    print(min(best, 2000000000))


if __name__ == "__main__":
    solution()
