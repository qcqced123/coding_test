import sys
from collections import deque
from itertools import combinations


def solution4():
    """
    idea: dfs + bfs
        - dfs: 그리드 좌표 25개에서 7개를 중복 없는 조합으로 뽑는 경우의 수 구하기
        - bfs: 구한 좌표 조합의 인접 여부, S가 4개 이상인지 여부
    """
    # bfs func
    def bfs(y: int, x: int, opp: int) -> int:
        q = deque([(y,x)])
        visited = {(y,x)}
        while q:
            vy, vx = q.popleft()
            for i in range(4):
                ny, nx = vy + dy[i], vx + dx[i]
                if -1 < ny < 5 and -1 < nx < 5 and (ny, nx) not in visited and (ny*5+nx) in comb:
                    if grid[ny][nx] == "Y":
                        opp += 1

                    if opp >= 4:
                        return 0

                    q.append((ny, nx))
                    visited.add((ny,nx))

        if len(visited) == 7: return 1
        else: return 0

    # init data structure
    input = sys.stdin.readline
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    grid = [list(input().rstrip()) for _ in range(5)]

    # get combinations
    answer = 0
    for comb in combinations(range(25), 7):
        opponent = 0
        y, x = divmod(comb[0], 5)
        if grid[y][x] == "Y":
            opponent += 1

        answer += bfs(y, x, opponent)

    print(answer)

if __name__ == "__main__":
    solution4()
