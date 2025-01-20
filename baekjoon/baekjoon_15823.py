import sys
from collections import defaultdict


def solution():
    """ 정렬 불가, 카드팩 == 좌우 연속 카드들 묶기, 카드팩 만들고 싶으면 구성 개수가 모두 동일, 같은 종류 카드 두장 x
    idea: two pointer with hash structure

    question:
        - 아니 NlogN 아래로 최적화 가능해??
    """
    # get input data
    input = sys.stdin.readline
    N, M = map(int, input().split())  # 카드 개수, 반드시 사야 되는 카드팩 개수
    arr = list(map(int, input().split()))

    # init cache
    curr = []
    cache = dict()
    for i, e in enumerate(arr):
        if e not in cache:
            cache[e] = len(curr)
            curr.append(e)
        else:
            curr = curr[cache[e]+1:]
            cache[e] = len(curr)
            curr.append(e)

        print(curr)
        print(cache)
        print()


if __name__ == "__main__":
    solution()
