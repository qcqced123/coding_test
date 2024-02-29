import sys
from typing import List


def solution():

    def inspecting(arr: List) -> int:
        def expand(l: int, r: int):
            while l > -1 and r < len(arr) and arr[l] == arr[r]:
                l -= 1
                r += 1
            return arr[l+1:r]

        cnt = ''
        for i in range(len(arr)-1):
            cnt = max(
                cnt,
                expand(i, i+1),
                expand(i, i+2),
                key=len
            )

        result = 1 if len(cnt) == len(arr) else 0
        return result

    N = int(sys.stdin.readline())
    array = [0] + list(map(int, sys.stdin.readline().split()))  # for matching number of index
    M = int(sys.stdin.readline())
    for _ in range(M):
        start, end = map(int, sys.stdin.readline().split())
        if start == end:
            print(1)
            continue
        print(inspecting(array[start:end+1]))


if __name__ == "__main__":
    solution()
