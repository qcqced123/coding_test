import sys


def solution():
    """ 사정 거리 안쪽 동물 숫자, NlogN
    사대 위치, 동물 위치, 사대별로 잡을 수 있는 동물 수를 리턴하라는거야?
    근데 사대 위치는 또 어떻게 처리해야 되냐

    idea: binary search
        - 사대, 동물 위치 배열 정렬
        - 탐색 범위/대상:
        - 포인터 이동 조건:
    question:
        - 사정거리랑 거리를 비교: 거리를 구하려면 사대별 & 동물 위치를 파악해야함, 이게 10만**2
        - 동물 숫자 배열을 이진 탐색해도, 어차피 10만**2를 피할 수 없음
        - 사대 위치에 대해서 탐색을 시키려고 해도... 그게 포인터 이동 조건 세팅이 안되서 힘듦
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
