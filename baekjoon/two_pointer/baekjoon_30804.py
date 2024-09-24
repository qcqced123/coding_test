import sys
from collections import defaultdict


def solution():
    """ sliding window solution
    """
    def expand(right: int, state: set):
        candidate = 1
        while right < len(candies):
            state.add(candies[right])
            if len(state) >= 3:
                break

            right += 1
            candidate += 1
        return candidate

    N = int(sys.stdin.readline())
    candies = list(map(int, sys.stdin.readline().split()))

    result = 0
    for i in range(len(candies)):
        cnt_dict = {candies[i]}
        result = max(
            result,
            expand(i+1, cnt_dict)
        )
    print(result)


def review_solution():
    def is_valid() -> int:
        flag = 0
        for i in cache.values():
            if i:
                flag += 1

        return 1 if flag < 3 else 0

    result = 1
    N = int(input())
    arr = list(map(int, sys.stdin.readline().split()))  # 탕후루 배열

    l, r = 0, 0
    cache = {k: 0 for k in set(arr)}
    cache[arr[l]] += 1

    while r < N-1:
        next_element = arr[r+1]
        cache[next_element] += 1
        if not is_valid():
            while not is_valid():
                out = arr[l]
                cache[out] -= 1
                l += 1

        # slicing is same as deepcopy in 1D-array, so do not use slicing for calculating length
        r += 1
        result = max(result, r - l + 1)

    print(result)


def review_optimize_solution():
    N = int(input())
    arr = list(map(int, sys.stdin.readline().split()))  # 탕후루 배열

    l, r = 0, 0
    cache = defaultdict(int)  # 숫자의 빈도를 저장할 딕셔너리
    cache[arr[l]] += 1

    result = 1
    num_kinds = 1  # cache_value
    while r < N-1:
        r += 1
        cache[arr[r]] += 1
        if cache[arr[r]] == 1:
            num_kinds += 1

        while num_kinds > 2:
            cache[arr[l]] -= 1
            if not cache[arr[l]]:
                num_kinds -= 1
            l += 1

        # slicing is same as deepcopy in 1D-array, so do not use slicing for calculating length
        result = max(result, r - l + 1)

    print(result)


if __name__ == "__main__":
    review_solution()
