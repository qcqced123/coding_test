import sys
from collections import deque


def solution():
    """ 추락, 테트리스 게임,
    같은 색 4개 이상 연결: 연결된 모든 뿌요 폭발
    "연쇄": 같은 턴, 서로 다른 시점에 폭발한 횟수

    idea: graph search with simulation
        - 게임 시물레이션 진행하면서, 최대 몇 번의 연쇄가 발생하는가 업데이트
        - outer loop: 연쇄 횟수
            - 그리드 상태 pause:
                - 연쇄 가능한 위치 검사 (0)
                - 연쇄 위치 리스트 만들기 (0)

            - 그리드 업데이트:
                - 연쇄 위치 모두 없애기 (0)
                - 공중에 떠있는 친구들 바닥으로 떨구기s

            - 다음 턴으로 이동
    feedback:
        - 호흡 길어지면 이상한 실수 개많이 하네 진짜;;
    """
    # bfs func
    def bfs(y: int, x: int, p: str) -> list:
        """
        Args:
            y: y index of current player
            x: x index of current player
            p: current player's name
        """
        result = [(y, x)]
        visited[y][x] = 1
        q = deque([(y, x)])
        while q:
            vy, vx = q.popleft()
            for i in range(4):
                ny, nx = vy + dy[i], vx + dx[i]
                if -1 < ny < 12 and -1 < nx < 6 and not visited[ny][nx] and grid[ny][nx] == p:
                    q.append((ny, nx))
                    result.append((ny, nx))
                    visited[ny][nx] = 1

        return result if len(result) >= 4 else None

    # do push the puyo
    def push(y: int, x: int, p: str) -> None:
        vy, vx = y, x
        while vy < 11:
            vy += 1
            if grid[vy][vx] != ".":
                grid[y][x] = "."
                grid[vy-1][vx] = p
                break

            elif vy == 11 and grid[vy][vx] == ".":
                grid[y][x] = "."
                grid[vy][vx] = p
                break

    # init the data structure
    input = sys.stdin.readline
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    grid = [list(map(str, input().strip())) for _ in range(12)]

    # simulation with bfs
    answer = 0
    players = ["R", "G", "B", "P", "Y"]
    while True:
        explode = []
        visited = [[0]*6 for _ in range(12)]
        for player in players:
            for y in range(12):
                for x in range(6):
                    if grid[y][x] == player and not visited[y][x]:
                        cnt = bfs(y, x, player)
                        if cnt is not None:
                            explode.append(cnt)

        # end point of conditional loop
        if not explode:
            print(answer)
            break

        for container in explode:
            for i,j in container:
                grid[i][j] = "."

        for x in range(6):
            for y in range(11, -1, -1):
                if grid[y][x] != ".":
                    push(y, x, grid[y][x])
        answer += 1


if __name__ == "__main__":
    solution()
