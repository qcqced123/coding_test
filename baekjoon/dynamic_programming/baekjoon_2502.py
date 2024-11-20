import sys


def solution():
    """ 에라이
    idea: dynamic programming
        - 근거 1: 어제 + 그저께 떡 개수 모두 캐싱 필요
    """
    input = sys.stdin.readline
    D, K = map(int, input().split())  # D일차, 떡개수
    for i in range(1, K+1):
        for j in range(i, K+1):
            cache = [0]*(D+1)
            cache[1] = i
            cache[2] = j
            for k in range(3, D+1):
                cache[k] = cache[k-1] + cache[k-2]

            if cache[D] == K:
                print(cache[1])
                print(cache[2])
                return


if __name__ == "__main__":
    solution()
