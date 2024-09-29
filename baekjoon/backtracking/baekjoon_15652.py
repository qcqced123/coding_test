import sys


def solution():
    """ 길이 M, 비내림차순 수열 출력
    idea:
    """
    def recursive_func(x: int, result):
        """
        Args:
            x: index
            result
        """
        if len(result) == M:
            print(*result)
            return

        for i in range(x, N):
            curr = result[:]
            curr.append(arr[i])
            recursive_func(i, curr)

        return

    sys.setrecursionlimit(10**6)
    N, M = map(int, sys.stdin.readline().split())
    arr = list(range(1, N+1))
    for i in range(1, N+1):
        recursive_func(i-1, [i])


if __name__ == "__main__":
    solution()
