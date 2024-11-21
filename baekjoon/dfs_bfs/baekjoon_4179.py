import sys
from collections import deque


def solution():
    """ 저번에 푼 불 문제랑 똑같네
    idea: simulation with bfs
        - 불 이동
        - 지훈이 이동
        - 방문 배열 제발 구현해
    """
    # init data structure
    input = sys.stdin.readline
    R, C = map(int, input().split())
    visited = [[0]*C for _ in range(R)]
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    grid = [list(map(str, input().rstrip())) for _ in range(R)]

    # find the initial point of each game player
    fires, player = [], []
    for y in range(R):
        for x in range(C):
            if grid[y][x] == "F": fires.append((y,x))
            elif grid[y][x] == "J": player.append((y,x))

    # do the simulation of game
    time, flag = 0, False
    fire_q, player_q = deque(fires), deque(player)
    while player_q:
        # fire move
        for i in range(len(fire_q)):
            vfy, vfx = fire_q.popleft()
            for j in range(4):
                nfy, nfx = vfy + dy[j], vfx + dx[j]
                if -1 < nfy < R and -1 < nfx < C:
                    if grid[nfy][nfx] == "." or grid[nfy][nfx] == "J":
                        grid[nfy][nfx] = "F"
                        fire_q.append((nfy, nfx))

        # player move
        for i in range(len(player_q)):
            vpy, vpx = player_q.popleft()
            for j in range(4):
                npy, npx = vpy + dy[j], vpx + dx[j]
                if -1 < npy < R and -1 < npx < C and not visited[npy][npx] and grid[npy][npx] == ".":
                    visited[npy][npx] = 1
                    player_q.append((npy, npx))

                elif not (-1 < npy < R and -1 < npx < C):
                    flag = True
        time += 1
        if flag:
            print(time)
            break
    else:
        print("IMPOSSIBLE")


if __name__ == "__main__":
    solution()
