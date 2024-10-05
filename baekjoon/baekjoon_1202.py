import sys
import heapq


def solution():
    """ 무게-가격 trade-off, 보석•가방 (NlogK)
    3 3
    3 100
    2 70
    5 40
    10
    2
    3

    idea: greedy with priority queue
        1) 보석으로 루프
        2) 루프마다 현재 가치가 가장 낮은, 가방 리턴, 가치가 모두 같으면, 무게 리미트가 순서로

    reference:
        https://www.acmicpc.net/problem/12865
        https://www.acmicpc.net/board/view/129125
    """
    N, K = map(int, sys.stdin.readline().split())  # 보석 개수, 가방 개수
    arr = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 무게, 가격

    h = []
    result = 0
    bag = [int(input()) for _ in range(K)]
    arr.sort(key=lambda x: (x[0], -x[1])), bag.sort()
    for k in bag:
        while arr and arr[0][0] <= k:  # 사실 이 부분이 의문임, 여기 최악의 경우 N인데
            heapq.heappush(h, -arr[0][1])
            heapq.heappop(arr)

        if h:
            result -= heapq.heappop(h)

    print(result)


if __name__ == "__main__":
    solution()
