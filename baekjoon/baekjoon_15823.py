import sys


def solution():
    """ <= NlogN
    idea: two-pointer with parametric search
        [two pointer]
        - 포인터 위치:
        - 포인터 방향:
        - 포인터 이동 방향:

        [parametric search]
        - 최적화 대상/범위: 카드팩을 구성하는 최대 카드 개수, 1 to int(N//M)
        - 최적화 기준: 현재 카드팩 개수 vs M

        [hash]
        - 단일 카드팩의 데이터 유일성 검사용

    feedback:
        -
    """
    # get input data
    input = sys.stdin.readline
    N, M = map(int, input().split())  # 카드 개수, 반드시 사야 되는 카드팩 개수
    arr = list(map(int, input().split()))

    # do parametric search with two-pointer algorithm
    answer = 0
    l, r = 1, int(N//M)
    while l <= r:
        mid = (l+r) // 2  # current standard value
        cnt, cards = 0, set()
        for card in arr:
            if card not in cards:
                cards.add(card)



if __name__ == "__main__":
    solution()
