import sys
from bisect import bisect_left


def solution():
    """
    idea: binary search
        - 제약: 총 K번 구매 가능, 하루에 한 번 가능, 직전 주식 매매한 가격 캐싱 필요(스택)
        - 가장 긴 증가하는 부분 수열 응용
        - 주어진 K에 해당 되는 길이의 부분 수열이 존재하는가 여부를 알려주기!
    """
    # init data structure
    input = sys.stdin.readline
    for t in range(int(input())):
        N, K = map(int, input().split())
        stocks = list(map(int, input().split()))

        # do bisect
        flag = 0
        frame = -1
        cache = []
        for i, stock in enumerate(stocks):
            if stock > frame:
                cache.append(stock)
                frame = stock

            else:
                idx = bisect_left(cache, stock)
                cache[idx] = stock
                frame = cache[-1]

            if len(cache) == K:
                flag += 1
                break

        print(f"Case #{t+1}", end='\n')
        print(flag)


if __name__ == "__main__":
    solution()
