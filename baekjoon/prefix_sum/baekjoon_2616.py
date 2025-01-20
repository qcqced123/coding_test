import sys


def solution():
    """ 소형 기관차 3대, 기존 객차 선택, 모든 객차 전체 선택은 불가능, 선택의 최적화 문제, NlogN
    idea: prefix sum
        - 사용한 소형 기관차 개수도 테이블 캐싱 필요 (3*N)
        - prefix[k][i]: k개의 소형 기관차를 사용하고, i번째 객차까지 고려했을 때, 최대 승객 숫자

    question:
        - 점화식을 어떻게 세워야 하는가 감이 안잡힘
            - dp 배열에 prefix 배열까지 점화식에 섞으라고?? 미친 개어렵네 진짜
    reference:
        - https://devjoy.tistory.com/265
    """
    # init data structure
    input = sys.stdin.readline
    N = int(input())
    people = [0] + list(map(int, input().split()))
    limit = int(input())
    dp = [[0]*(N+1) for _ in range(4)]  # add the dummy row, column

    # do prefix sum
    prefix = [0]*(N+1)
    for i in range(1, N+1):
        prefix[i] = prefix[i-1] + people[i]

    # do dynamic programming
    for i in range(1, 4):
        for j in range(limit, N+1):
            dp[i][j] = max(dp[i][j-1], dp[i-1][j-limit] + prefix[j] - prefix[j-limit])

    print(dp[3][N])


if __name__ == "__main__":
    solution()
