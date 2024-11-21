import sys


def solution():
    """ 전투력 순서 == 배치 순서, 원소를 최소한으로 빼서, 감소하는 수열 만들기, N**2
    idea: dynamic programming
        - double for-loop
        - 감소하는 부분 수열!
        - answer = 전체 수열 길이 - 감소하는 부분 수열에서 제외되는 친구들 개수
    """
    # init the data structure
    input = sys.stdin.readline
    N = int(input())
    cache = [1]*N
    arr = list(map(int, input().split()))

    # update the cache
    for i in range(1, N):
        cnt = arr[i]
        for j in range(i):
            if arr[j] > cnt:
                cache[i] = max(cache[i], cache[j] + 1)

    answer = N - max(cache)
    print(answer)


if __name__ == "__main__":
    solution()
