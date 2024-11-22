import sys
from bisect import bisect_left


def solution():
    """ 가장 긴 증가 하는 연속 부분 수열, NlogN
    idea: binary search with stack
        - 이게 이분 탐색이 필요할까??
        - 그냥 작은거 등장하면, 캐시 초기화하고 세어주면 되는거 아닐까??
        - "연속"이라는걸까 아닐까...? 문제 조건 써있는게 불명확해...
        - 시간 복잡도 고려하면, 그냥 가장 긴 증가하는 부분 수열 가틈
    """
    input = sys.stdin.readline
    while True:
        try:
            N = int(input())
            stocks = list(map(int, input().split()))
            frame, cache = -1, []
            for stock in stocks:
                if stock > frame:
                    cache.append(stock)
                    frame = stock

                else:
                    idx = bisect_left(cache, stock)
                    cache[idx] = stock
                    frame = cache[-1]
            print(len(cache))

        except:
            break


if __name__ == "__main__":
    solution()
