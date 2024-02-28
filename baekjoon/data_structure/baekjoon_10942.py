import sys
from typing import List


def solution():
    sys.setrecursionlimit(10**6)
    N = int(sys.stdin.readline())
    _ = list(map(int, sys.stdin.readline().split()))
    postorder = list(map(int, sys.stdin.readline().split()))
    result = []
    def preorder(src: int, end: int):
        if src < end:
            return

        root = postorder[src]
        new_left = src-1
        for i in range(src-1, end-1, -1):
            if postorder[i] < root:
                new_left = i
                break

        result.append(root)
        preorder(new_left, end)
        preorder(src-1, new_left+1)

    preorder(N-1, 0)
    print(*result)


if __name__ == "__main__":
    solution()
