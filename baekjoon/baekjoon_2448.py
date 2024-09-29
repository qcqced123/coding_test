import sys


def solution():
    """
    1) N = 2^k*3
            - k가 1 커질수록, 직전 프린팅의 세 배
    2) N에 대해서 마지막 N번째 줄의 필요한 원소 숫자는 2N-1
    idea: divide and conquer
        1) 출력용 배열 초기화
            - 첫줄:
    """

    def recursive_func():
        return

    N = int(input())
    sys.setrecursionlimit(10 ** 6)

    arr = [[0] * (2 * N - 1) for _ in range(2 * N - 1)]
    for i in range(len(arr)):
        print(arr[i], end='\n')



if __name__ == "__main__":
    solution()
