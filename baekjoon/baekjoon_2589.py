import sys
from collections import deque


def solution():
    """ 상하좌우, 육지로만, 보물 to 보물 (시작 to 종점) 최단 거리
    idea: 인접 배열 탐색, bfs
        - 보물이 묻힌 곳부터 정해야함
            - 노드 to 노드가 가장 먼쌍에 보물이 묻혀있음
            - 그럼 육지마다 bfs를 수행하면서 최장 거리 찾아야지
        - 최단 거리: bfs가 유리함

    feedback:
        - 파이썬이 처느려서, pypy로만 되는듯
            - 게시판 보니까, 예외처리를 좀 해주면 python3도 통과 ㄴ한다는데, 생각 안나니까 답지 보자
    """
    # init the data structure
    input = sys.stdin.readline
    R, C = map(int, input().split())
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    grid = [list(map(str, input().rstrip())) for _ in range(R)]

    # update the answer with the bfs search for each land nodes
    def bfs(y: int, x: int) -> int:
        # init the data structure for bfs
        d = 0
        q = deque([(y,x,0)])
        visited = set()
        visited.add((y,x))

        while q:
            vy, vx, vd = q.popleft()
            d = max(d, vd)

            for i in range(4):
                ny, nx = vy + dy[i], vx + dx[i]
                if -1 < ny < R and -1 < nx < C and grid[ny][nx] == "L" and (ny,nx) not in visited:
                    visited.add((ny,nx))
                    q.append((ny,nx,vd+1))

        return d

    answer = 0
    for y in range(R):
        for x in range(C):
            if grid[y][x] == "L":
                answer = max(answer, bfs(y,x))
    print(answer)


if __name__ == "__main__":
    solution()
