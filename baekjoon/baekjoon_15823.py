import sys


def solution():
    """ 정렬 불가, 카드팩 == 좌우 연속 카드들 묶기, 카드팩 만들고 싶으면 구성 개수가 모두 동일해야 함, 같은 종류 카드 두장 x
    idea: parametric search with hash structure (set)
        - 최적화 대상/범위: 카드팩을 구성하는 최대 카드 숫자, 1 to int(N//M)
        - 최적화 기준:
    question:
        - 아직 개수 다 못채우고, 겹치는거 찾았을 때, "in" 연산 안하고 겹치는거 위치 찾아서, 뒷부분만 남기는게 될까?? 세트??
    """
    input = sys.stdin.readline
    N, M = map(int, input().split())  # 카드 개수, 반드시 사야 되는 카드팩 개수
    arr = list(map(int, input().split()))

    # do parametric search
    answer = 0
    l, r = 1, int(N//M)
    while l <= r:
        group = 0
        cache = set()
        mid = (l + r) // 2
        for element in arr:
            if element not in cache:
                cache.add(element)
                if len(cache) == mid:
                    group += 1
                    cache.clear()
            else:

                cache.clear()

        if group >= M:
            if group == M: answer = mid
            l = mid + 1
        else:
            r = mid - 1

    print(answer)

if __name__ == "__main__":
    solution()
