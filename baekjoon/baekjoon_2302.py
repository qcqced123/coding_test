import sys


def solution():
    """ VIP 고정, 일반 회원들 경우의 수
    일반 회원: 본인 좌석 or 바로 옆으로 이동
    VIP: 본인 좌석만

    idea:

    question:
        - 그냥 문제가 이해 안감
    """
    input = sys.stdin.readline
    N = int(input())
    vips = [int(input()) for _ in range(N)]


if __name__ == "__main__":
    solution()
