import sys
from collections import deque


def purifier():
    for y in range(r):
        for x in range(c):
            pd = grid[y][x]  # purifier dust
            if (y == 0 or y == r-1) and x and pd > 0:  # 가로 양 끝 처리
                grid[y][x] = 0
                purifier_list.append([pd, y, x-1])

            elif (y == top or y == bottom) and 0 < x < c-1 and pd > 0:  # same row index with top purifier
                grid[y][x] = 0
                purifier_list.append([pd, y, x+1])

            elif y <= top and x == c-1 and pd > 0:
                grid[y][x] = 0
                purifier_list.append([pd, y-1, x])

            elif y >= bottom and x == c - 1 and pd > 0:
                grid[y][x] = 0
                purifier_list.append([pd, y+1, x])

            elif y < top and x == 0 and pd > 0:
                if y+1 == top:
                    grid[y][x] = 0
                    continue
                grid[y][x] = 0
                purifier_list.append([pd, y+1, x])

            elif y > bottom and x == 0 and pd > 0:
                if y-1 == bottom:
                    grid[y][x] = 0
                    continue
                grid[y][x] = 0
                purifier_list.append([pd, y-1, x])

            elif pd > 0:
                next_list.append([pd, y, x])


def diffusion(d: int, y: int, x: int):
    count = 0
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    nd = int(d / 5)
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if -1 < ny < r and -1 < nx < c and grid[ny][nx] > -1:
            count += 1
            apply_list.append([nd, ny, nx])
    ld = d - count * nd  # left dust
    return ld


r, c, t = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]
top, bottom = [i for i in range(2, r-2) if grid[i][0] == -1]  # check air purifier index


queue = deque([])
for y in range(r):
    for x in range(c):
        dust = grid[y][x]
        if dust > 4:
            queue.append([dust, y, x])
while t:
    apply_list, purifier_list, next_list = [], [], []
    for _ in range(len(queue)):
        vd, vy, vx = queue.pop()
        ld = diffusion(vd, vy, vx)
        grid[vy][vx] = ld

    for task in apply_list:
        ad, ay, ax = task[0], task[1], task[2]  # apply dust, y, x
        grid[ay][ax] += ad

    purifier()
    for p_task in purifier_list:
        pd, py, px = p_task[0], p_task[1], p_task[2]
        grid[py][px] = pd
        queue.append(p_task)

    for n_task in next_list:
        queue.append(n_task)
    t -= 1
print(sum(list(map(sum, grid))) + 2)  # for purifier