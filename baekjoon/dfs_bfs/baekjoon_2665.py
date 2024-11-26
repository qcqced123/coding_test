import sys
from collections import deque


def solution():
    """ 검은방 == 벽, 검은방 바꾸는 경우를 최소화, 최단 경로 만들기
    idea: bfs
        - 최단 경로를 구하되, 지나가면서 부순 검은방 개수 최소 경로 찾기
        - 부순 방 개수를 방문 배열에 직접 기록하자
            - 이러면, 방문 배열 초기화를 뭘로 하는지 중요해짐
            - 0 으로 해도 될 듯
    """
    # init the data structure
    INF = sys.maxsize
    input = sys.stdin.readline
    N = int(input())
    visited = [[-1]*N for _ in range(N)]
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    grid = [list(map(str, input().rstrip())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            grid[i][j] = int(grid[i][j])

    # do bfs
    answer = INF
    q = deque([(0, 0)])
    visited[0][0] = 0
    while q:
        vy, vx = q.popleft()
        vb = visited[vy][vx]
        for i in range(4):
            ny, nx = vy + dy[i], vx + dx[i]
            if ny == N-1 and nx == N-1:
                answer = min(answer, visited[vy][vx])
                continue

            if -1 < ny < N and -1 < nx < N and vb < answer:
                if not grid[ny][nx] and (visited[ny][nx] == -1 or vb+1 < visited[ny][nx]):
                    visited[ny][nx] = vb + 1
                    q.append((ny, nx))

                elif grid[ny][nx] and (visited[ny][nx] == -1 or vb < visited[ny][nx]):
                    visited[ny][nx] = vb
                    q.append((ny, nx))
    print(answer)


if __name__ == "__main__":
    solution()
