import sys


def solution():
    """ NlogN...?
    석순: 바닥 to 천장
    종유석: 천장 to 바닥

    idea: two pointer, binary search
        - 석순이랑 종유석 단위 통일
        - 탐색 대상/범위: 구간 배열, 0 to max*2
        - 탐색 기준
    """
    input = sys.stdin.readline
    N, H = map(int, input().split())  # 장애물 숫자, 길이
    height = [int(input()) for _ in range(N)]



if __name__ == "__main__":
    solution()
