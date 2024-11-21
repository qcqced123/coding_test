import sys
from collections import deque


def solution():
    """
    idea: graph search, adj array
        - 불부터 이동
        - 더블 큐
        - outer loop: 시간

    feedback:
        - 제발 방문 배열좀.... 왜 자꾸 중복으로 큐에 처넣는거지....?
    """
    # init data structure
    visited = set()
    input = sys.stdin.readline
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    for _ in range(int(input())):
        c, r = map(int, input().split())  # 열크기, 행크기
        grid, player, fires = [], [], []
        for i in range(r):
            col = list(map(str, input().rstrip()))
            for j in range(c):
                if col[j] == "@": player.append((i,j))
                elif col[j] == "*": fires.append((i,j))

            grid.append(col)

        # do simulation
        visited.add((player[0][0], player[0][1]))
        time, flag = 0, False
        fire_q = deque(fires)
        player_q = deque(player)
        while player_q:
            for i in range(len(fire_q)):
                vfy, vfx = fire_q.popleft()
                for j in range(4):
                    nfy, nfx = vfy + dy[j], vfx + dx[j]
                    if -1 < nfy < r and -1 < nfx < c and (grid[nfy][nfx] == "." or grid[nfy][nfx] == "@"):
                        grid[nfy][nfx] = "*"
                        fire_q.append((nfy, nfx))

            for i in range(len(player_q)):
                vpy, vpx = player_q.popleft()
                for j in range(4):
                    npy, npx = vpy + dy[j], vpx + dx[j]
                    if -1 < npy < r and -1 < npx < c and (npy, npx) not in visited and grid[npy][npx] == ".":
                        visited.add((npy,npx))
                        player_q.append((npy, npx))
                    elif not (-1 < npy < r and -1 < npx < c):
                        flag = True
                        break
            time += 1
            if flag:
                print(time)
                break
        else:
            print("IMPOSSIBLE")

        visited.clear()


if __name__ == "__main__":
    solution()
