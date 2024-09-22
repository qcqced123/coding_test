import sys


def solution():
    """ 연속된 수열의 부분합, 합이 S 이상, 길이는 가장 짧은, 길이 리턴, NlogN
    idea: two pointer
        1) 포인터 위치 초기화
            - 포인터 위치: 나란히 (가장 짧은 길이를 찾아야 하기 때문에)
            - 포인터 방향: forward
            - 포인터 이동 조건:
                - > S: left pointer forward
                - < S: right pointer forward
    """
    best = sys.maxsize
    N, S = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))

    l, r = 0, 0  # 겹치는 위치에서 시작 가능
    cache = arr[l]
    l_cache, r_cache = l, r
    while r < N:
        if r != r_cache:
            r_cache = r
            cache += arr[r]

        elif l != l_cache:
            l_cache = l
            cache -= arr[l-1]

        if cache < S:
            r += 1

        else:
            best = min(best, len(arr[l:r+1]))
            l += 1

    print(best if best != sys.maxsize else 0)


if __name__ == "__main__":
    solution()
