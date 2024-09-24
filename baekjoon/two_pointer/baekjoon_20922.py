import sys


def solution():
    """ 같은 원소가 K개 이하, 최장 연속 부분 수열 길이, NlogN

    idea:
        1) 포인터 설정 초기화:
            - 포인터 위치: 나란히
            - 포인터 이동 방향: forward
            - 포인터 이동 조건:
                - =< K: right forward
                - > K: left forward
        2) 포인터 이동할 떄마다 부분 수열 내부 조사
            - 초기값 구해놓고, 새로운 포인터 위치에 대한 변경 내용만 반영 (초기값은 뭘로...?)
            - 사전 써야겠네
    """
    result = 1
    N, K = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))

    l, r = 0, 0
    cache = {k: 0 for k in set(arr)}
    cache[arr[l]] += 1

    cache_state = True  # True: cache can get the new element from array
    while r < N-1:
        next_element = arr[r+1]
        if cache[next_element] >= K:
            cache_state = False

        if cache_state:
            r += 1
            cache[arr[r]] += 1
            # slicing is same as deepcopy in 1D-array, so do not use slicing for calculating length
            result = max(result, r - l + 1)

        # while loop: value of next_element in cache under the K
        else:
            while cache[next_element] >= K:
                out = arr[l]
                cache[out] -= 1
                l += 1
            cache_state = True

    print(result)


if __name__ == "__main__":
    solution()
