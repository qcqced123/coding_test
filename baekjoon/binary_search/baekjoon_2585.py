import sys
from collections import deque


def solution():
    """
    idea: bfs with binary search
        연료통 값을 귀납적으로 찍기
        - 탐색 대상/범위: 연료통 값 배열, 0 to 목적지까지 필요 연료량
        - 탐색 기준:

    grid[y][x]:
        - y to x distances, 경유지 K개, y to x, 큐에 넣을 땐 x가 y가 되어야!

    bfs move rule:
        - 현재 y는 고정, x 쪽으로만 이동 하면서 limit에 맞는 곳이 어딘지 확인!
        - x == -1이 가능, 종료
        - y축 번호를 경유지 개수로 해석할 수 있겠군...
        - 굳이 거리를 또 재서 빼고 말고 할 필요도 없구나, 어차피 큐에 그 노드를 넣는다는게 급유를 한다는 의미가 되어서...

    feedback:
        - 이걸 bfs로 풀 생각을 전혀... 못함...
        - 이정도 수준이 하나는 나올텐데... ㅜ
    """
    def cal_distance(y, x) -> int:
        """helper func for calculating the minimum energy, y to x node"""
        sy, sx = airports[y]
        ey, ex = airports[x]
        d = pow((sy-ey)**2 + (sx-ex)**2, 1/2)
        return int((d//10)+1 if d % 10 else d//10)

    # do bfs
    def bfs(limit: int) -> int:
        q = deque([(0, 0)])
        visited = set()
        visited.add(0)
        while q:
            vy, vx = q.popleft()
            # 현재 노드에서 도착지에 도달 가능한 경우, 종료
            if distances[vy][N+1] <= limit:
                return 1

            # 큐에 남은 다른 경우의 수도 계산을 해봐야 하니까, break X
            # 더 이상 경유를 못하기 떄문
            # 여기 개수 세는 부분이 잘 이해가 안감
            if vx >= K:
                continue

            for nx in range(1, N+2):
                if nx not in visited and distances[vy][nx] <= limit:
                    visited.add(nx)
                    q.append((nx, vx+1))  # 경유지 하나 통과했다는 의미!
        return 0

    # init data structure
    input = sys.stdin.readline
    N, K = map(int, input().split())
    airports = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(N)] + [(10000, 10000)]
    distances = [[0]*(N+2) for _ in range(N+2)]  # for 2d grid array

    # init the grid value by calculating the distances of each nodes to minimum energy
    for y in range(N+2):
        for x in range(N+2):
            distances[y][x] = cal_distance(y, x)

    # do bisect with bfs
    answer = 0
    l, r = 0, distances[0][-1]
    while l <= r:
        mid = (l+r) // 2
        if bfs(mid):
            answer = mid
            r = mid - 1
        else:
            l = mid + 1

    print(answer)

    for y in range(N+2):
        print(distances[y], end='\n')


if __name__ == "__main__":
    solution()
