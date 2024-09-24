import sys


def solution():
    """ 용액 세 개 합성, (N^2)
    idea: two pointer

        1) 배열 정렬
        2) 포인터 초기화:
            - 포인터 위치: 서브 배열의 양 끝
            - 포인터 이동 방향: forward, backward
            - 포인터 이동 조건:
                - > 0: right backward
                - < 0: left backward

    """
    N = int(input())
    chemical = list(map(int, sys.stdin.readline().split()))
    chemical.sort()

    best, record = sys.maxsize, None
    for i in range(N-1):
        mid = chemical[i]
        l = i+1
        r = N-1
        while l < r:
            cnt = mid + chemical[l] + chemical[r]
            flag = abs(cnt)
            if best > flag:
                best = flag
                record = [chemical[l], mid, chemical[r]]

            if cnt >= 0:
                r -= 1

            else:
                l += 1

    record.sort()
    for j in record:
        print(j, end=' ')


if __name__ == "__main__":
    solution()
