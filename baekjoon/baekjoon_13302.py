import sys


def solution():
    """ 경로별 쿠폰 개수 캐싱 필요,
    idea: dynamic programming

    question:
        - 쿠폰이 3장 이상 쌓였을 때, 꽁짜를 언제 쓸지 타이밍
        - 쿠폰 캐싱 방법...
    """
    # get input data
    input = sys.stdin.readline
    N, M = map(int, input().split())
    if M > 1: holiday = list(map(int, input().split()))
    elif M == 1: holiday = [int(input())]

    # init dp cache
    dp = []

if __name__ == "__main__":
    solution()
