import sys


def solution():
    """
    idea: dynamic programming
        - backtrack으로 풀기에는 최대 64자리 까지라서 못풀어
        - 점화식 세우기 개귀찮은데...?
        - 2D Table
            - 행: 0~9
            - 열: 자리수
    """
    # init data structure, update the dp cache
    input = sys.stdin.readline
    for _ in range(int(input())):
        n = int(input())
        cache = [1]*10
        for i in range(n-1):
            for j in range(10):
                cache[j] = sum(cache[j:])

        print(sum(cache))


if __name__ == "__main__":
    solution()
