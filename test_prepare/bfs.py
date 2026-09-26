"""
bfs

1)
"""
def solution1():
    """ 긴급통로, Day 6 아침 문제
    problem:
        - 상하좌우 이동 가능, 한 칸씩
        - 벽을 한 번 뚫을 수 있음 (이것도 이동 횟수에 포함되어야 함)

    idea: 3D bfs

    """
    from collections import deque

    # bfs func
    def bfs(y,x):
        q = deque()
        q.append((y,x,0))
        dist = [[[-1]*2 for _ in range(M)] for _ in range(N)]

        dist[y][x][0] = 0

        """
        y,x: 좌표
        s: state, 벽을 뚫었나 안뚫었나
        """
        while q:
            y,x,s = q.popleft()

            for d in range(4):
                ny, nx = y + dy[d], x + dx[d]

                if not (-1 < ny < N and -1 < nx < M):
                    continue

                if grid[ny][nx] == 0:
                    if dist[ny][nx][s] == -1:  # not visited
                        q.append((ny,nx,s))
                        dist[ny][nx][s] = dist[y][x][s] + 1
                        
                else:
                    if (s == 0 and dist[ny][nx][1] == -1):
                        q.append((ny,nx,1))
                        dist[ny][nx][1] = dist[y][x][s] + 1

        # get answer from bfs result
        candidate_1 = dist[N-1][M-1][0]
        candidate_2 = dist[N-1][M-1][1]

        if candidate_1 == -1:
            return candidate_2

        if candidate_2 == -1:
            return candidate_1

        return min(candidate_1, candidate_2)
    
    # get input
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    # direction vector
    dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

    # bfs interface
    answer = bfs(0,0)

    return answer


if __name__ == "__main__":
    print(solution1())