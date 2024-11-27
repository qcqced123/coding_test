import sys
from bisect import bisect_right


def solution():
    """
    idea: dynamic programming with binary search
        - pictures 배열 오름 차순 정렬
            - 1순위: 높이, 2순위: 비용

        - 개별 그림마다 높이 제약(S) 만족 하는 최대 인덱스 구하기 (bisect_right)
            - 정렬해서, 높이는 같지만 비용은 더 큰 친구들이 오른쪽에 놓이기 때문에 right를 사용해야 정확하다
            - right로 얻어낸 인덱스 값에 해당되는 위치의 그림의 높이가 제약 조건과 다르면 1을 빼준 값을 기록

        - 점화식 이용해서 dp 캐시 업데이트
            - 직전 그림까지의 최대값 vs 현재 그림을 팔 수 있다고 가정하고, 해당 그림과 제약조건을 만족하는 그림까지의 최대 비용을 캐싱
    feedback:
        - 진짜 어려운데, 좋은 문제라고 생각함
    """

    # init the data structure
    input = sys.stdin.readline
    N, S = map(int, input().split())
    pictures = [(0,0)] + [tuple(map(int, input().split())) for _ in range(N)]
    pictures.sort()  # 높이랑 비용도 같이 오름차순으로 정렬 되어야 함!!

    # init the height array
    cnt = [pictures[i][0] for i in range(N+1)]
    heights = [0]*(N+1)
    for i, (ph, pc) in enumerate(pictures):
        idx = bisect_right(cnt, ph-S)
        if ph-S != cnt[idx]: idx -= 1
        heights[i] = idx

    # do update the dp cache with bisect
    cache = [0]*(N+1)
    for i in range(1, N+1):
        j = heights[i]
        cache[i] = max(cache[i-1], cache[j]+pictures[i][1])

    print(max(cache))


if __name__ == "__main__":
    solution()
