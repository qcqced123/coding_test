import sys


def solution():
    """ 사정 거리 안쪽 동물 숫자, NlogN
    사대 위치, 동물 위치, 사대별로 잡을 수 있는 동물 수를 리턴하라는거야?
    근데 사대 위치는 또 어떻게 처리해야 되냐

    idea: binary search
        - 사대, 동물 위치 배열 정렬
        - 탐색 범위/대상:
        - 포인터 이동 조건:

    """
    input = sys.stdin.readline
    M, N, L = map(int, input())  # 사대, 동물, 사저어리

    gun_pos = list(map(int, input().split()))
    animal_pos = [list(map(int, input().split())) for _ in range(N)]

    gun_pos.sort(), animal_pos.sort()

    l, r = 0, N
    while l <= r:
        mid = (l+r) // 2


if __name__ == "__main__":
    solution()
