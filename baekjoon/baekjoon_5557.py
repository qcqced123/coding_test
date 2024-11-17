import sys


def solution():
    """
    idea: dynamic programming
        - 2D Table
            - 행: 피연산자
            - 열: 제약조건 (모든 계산 결과는 반드시 0 to 20 사이)
                - 0부터 20 나열
        - 이렇게 보니까 기타 리스트 문제랑 거의 비슷함

    question:
        - dp table 정의 자체를 못 하겠다
    """
    # init the data structure
    input = sys.stdin.readline
    N = int(input())
    cache = [[0]*21 for _ in range(N-1)]
    numbers = list(map(int, input().split()))
    numbers, target = numbers[:-1], numbers[-1]

    # do update the dp cache array
    src = numbers[0]
    cache[0][src] = 1
    for i in range(1, N-1):
        cnt = numbers[i]
        for j in range(21):
            if j + cnt <= 20:
                cache[i][j] += cache[i-1][j+cnt]

            if j - cnt >= 0:
                cache[i][j] += cache[i-1][j-cnt]

    print(cache[-1][target])

if __name__ == "__main__":
    solution()
