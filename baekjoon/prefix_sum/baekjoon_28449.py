import sys
from bisect import bisect_left, bisect_right


def solution():
    """ NlogM + MlogN
    idea: bisect with parametric search
        - 둘 다 정렬
        - Hi 팀 선형 탐색하면서 bisect
    """
    input = sys.stdin.readline
    N, M = map(int, input().split())
    HI = list(map(int, input().split()))
    ARC = list(map(int, input().split()))
    size = len(ARC)

    # do sort by ascending
    HI.sort(), ARC.sort()

    # do bisect with linear search
    win_h, win_a, draw = 0, 0, 0
    for player in HI:
        l, r = bisect_left(ARC, player), bisect_right(ARC, player)
        # count draw situation
        if l != r:
            draw += r - l
        else:
            if l < size and player == ARC[l]:
                draw += 1
                r += 1

        win_h += l
        win_a += size-r

    print(win_h, win_a, draw)


if __name__ == "__main__":
    solution()
