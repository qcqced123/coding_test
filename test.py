test = [1,2,3,4,5]
hp = test[0]
hp -= 1

print(hp)
print(test)


arr = []
print(arr[1])


import sys
from collections import deque
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
                if -1 < npy < r and -1 < npx < c:
                    if grid[npy][npx] == ".":
                        player_q.append((npy, npx))
                else:
                    flag = True
                    break
        time += 1
        if flag:
            print(time)
            break
    else:
        print("IMPOSSIBLE")

