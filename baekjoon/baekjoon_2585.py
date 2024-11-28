import sys
from collections import deque, defaultdict


def solution():
    """
    idea: bfs with binary search
        연료통 값을 귀납적으로 찍기
        - 탐색 대상/범위: 연료통 값 배열, 0 to 목적지까지 필요 연료량
        - 탐색 기준:

    feedback:
        - 이걸 bfs로 풀 생각을 전혀... 못함...
        - 이정도 수준이 하나는 나올텐데... ㅜ
    """
    # init data structure
    input = sys.stdin.readline
    N, K = map(int, input().split())
    airports = [tuple(map(int, input().split())) for _ in range(N)]


if __name__ == "__main__":
    solution()
