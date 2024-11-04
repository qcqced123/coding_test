import sys


def solution():
    """ NlogN...?
    석순: 바닥 to 천장
    종유석: 천장 to 바닥

    [0,1]
    [5,10]
    [0,3]
    [7,10]
    [0,5]
    [9,10]

    [0,1]
    [0,3]
    [0,5]
    [5,10]
    [7,10]
    [9,10]

    idea: two pointer, binary search
        - 석순이랑 종유석 단위 통일
        - sorting
    """
    input = sys.stdin.readline
    N, H = map(int, input().split())  # 장애물 숫자, 길이
    height = [int(input()) for _ in range(N)]




if __name__ == "__main__":
    solution()
