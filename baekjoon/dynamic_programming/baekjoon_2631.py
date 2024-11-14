import sys


def solution():
    """ 줄 세우기, 최소 변경
    idea: dynamic programming
        - 수열 길이 - 가장 긴 증가하는 부분 수열 개수
        - 가장 긴 증가하는 부분 수열:
            - 시간 복잡도 여유가 있어서 dynamic programming (N**2)으로 풀이 가능

    question:
        - 그냥 접근 방법이 감도 안옴

    feedback:
        - 생각해보니까 간단하구나
        - 주어진 수열에서 가장 긴 증가하는 부분 수열에 해당 되는 애들 말고는 다 옮겨야함
    """
    input = sys.stdin.readline
    N = int(input())
    cache = [1]*N
    arr = [int(input()) for _ in range(N)]

    # do init the dynamic programming
    for i in range(1, N):
        for j in range(i):
            if arr[i] > arr[j]:
                cache[i] = max(cache[i], cache[j] + 1)

    print(N-max(cache))


if __name__ == "__main__":
    solution()
