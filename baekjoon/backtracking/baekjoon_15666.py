import sys


def solution():
    """
    idea:
    """
    def recursive_func(x: int, result: list) -> None:
        if len(result) == M:
            if result not in cache:
                cache.append(result)
            return

        for i in range(x, N):
            curr = result[:]
            curr.append(arr[i])
            recursive_func(i, curr)

        return

    N, M = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()

    cache = []
    for i in range(N):
        recursive_func(i, [arr[i]])

    for j in cache:
        print(*j, end="\n")

if __name__ == "__main__":
    solution()
