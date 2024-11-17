import sys


def solution():
    """ 배열의 원소 세개 합, 해당 합이 배열에 존재 하는 것 중에 최대
    dynamic programming 혹은 binary search로 풀어야 되는데
    전자는 N**3으로 풀어야 해서, 복잡하니까 후자로 해보자

    idea: binary search with two-pointer
        - 탐색 대상/범위: 최대값 d의 경우의 수 배열, 0 to max(arr) (이거 인덱스로 돌려야 빠르겠다)
        - 탐색 기준: 세 수의 합이 배열에 있나 없나 검사
    [반례]
    5
    1
    2
    3
    7
    21
    >> 21

    6
    1
    2
    3
    4
    11
    20
    >> 11
    """
    input = sys.stdin.readline
    N = int(input())
    arr = [int(input()) for _ in range(N)]
    arr.sort()

    # do binary search with two pointer
    answer = 0
    l, r = 0, N-1
    while l <= r:
        temp = 0
        mid = (l+r) // 2
        cache = arr[mid]
        # do the two pointer search in sub sequence of array
        for i in range(mid):
            cnt = arr[i]
            left = i
            right = mid-1
            while left <= right:
                curr = cnt + arr[left] + arr[right]
                temp = max(temp, curr)
                if curr > cache:
                    right -= 1

                elif curr == cache:
                    answer = cache
                    break

                else:
                    left += 1

            if answer == cache:
                break

        if temp >= cache:
            l = mid + 1

        else:
            r = mid - 1

    print(answer)


def solution2():
    """ idea: only two-pointer
    """
    input = sys.stdin.readline
    N = int(input())
    arr = [int(input()) for _ in range(N)]
    arr.sort()

    # do the two pointer search
    answer = 0
    for i in range(N-1, 0, -1):
        cache = arr[i]
        for j in range(i):
            cnt = arr[j]  # 고정 위치
            left = j
            right = i - 1
            while left <= right:
                curr = cnt + arr[left] + arr[right]
                if curr > cache:
                    right -= 1

                elif curr == cache:
                    answer = cache
                    break

                else:
                    left += 1

        if answer == cache:
            break

    print(answer)


if __name__ == "__main__":
    solution2()
