import sys


def solution():
    """ 펌프 게임, 두 발은 서로 다른 지점 위치
    발 동시 못 움직임: 이터레이션 한 번에 발 하나만
    이전 위치에 따라서 다음 위치로 가는 에너지가 달라짐: 이동에 가중치
        1) 중앙 to 나머지: 2
        2) 인접 to 인접: 3
        3) 반대편: 4
        4) 같은 지점: 1

    100,000,000 (NlogN)
    idea:
    """
    UP, LEFT, DOWN, RIGHT = 1, 2, 3, 4
    *arr, _ = list(map(int, sys.stdin.readline().split()))


if __name__ == "__main__":
    solution()
