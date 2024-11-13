import sys


def solution():
    """ 금액 지불하는 경우의 수 구하는 문제랑 같음, N**2
    idea: dynamic programming
        - 인덱스 + 1: 카드 개수
        - 원소: 금액
        - 이중 루프 활용
    """
    input = sys.stdin.readline
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    cache = arr[:]

    # redefine the dp cache array
    for i in range(1, N+1):
        for j in range(1, i):
            cache[i] = min(cache[i], cache[j] + cache[i-j])

    print(cache[-1])


if __name__ == "__main__":
    solution()
