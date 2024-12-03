import sys


def solution():
    """
    idea: binary search
        - 주어진 값을 적당히 할당, 전체 배열의 최소값이 최대가 되도록
        - 탐색 대상: 배열의 최소값의 최대값 배열
        - 탐색 기준: 현재값을 최소값으로 만드는데 필요한 레벨값

    """
    input = sys.stdin.readline
    N, K = map(int, input().split())
    arr = [int(input()) for _ in range(N)]

    # do bisect
    answer = 0
    l, r = 1, max(arr) + K
    while l <= r:
        mid = (l+r) // 2
        cnt = 0
        for char in arr:
            if char < mid:
                cnt += mid - char

            if cnt > K:
                break

        if cnt > K:
            r = mid - 1
        else:
            l = mid + 1
            answer = mid

    print(answer)



if __name__ == "__main__":
    solution()
