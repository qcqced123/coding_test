import sys
from bisect import bisect_left


def solution():
    """
    idea: dynamic programming with binary search
        - 길이 오름 차순 정렬
        - height 배열 초기화 with bisect
        - height 배열 이용, dp cache 업데이트
    """
    # init the data structure
    input = sys.stdin.readline
    N, S = map(int, input().split())
    pictures = [(0,0)] + [tuple(map(int, input().split())) for _ in range(N)]
    pictures.sort()

    # init the height array
    cnt = [pictures[i][0] for i in range(N+1)]
    heights = [0]*(N+1)
    for i, (ph, pc) in enumerate(pictures):
        idx = bisect_left(cnt, ph-S)
        if ph-S == cnt[idx]: idx += 1
        heights[i] = idx

    # do update the dp cache with bisect
    cache = [0]*(N+1)
    for i in range(1, N+1):
        j = heights[i]
        cache[i] = max(cache[i], cache[j]+pictures[i][1])
    print(max(cache))


if __name__ == "__main__":
    solution()
