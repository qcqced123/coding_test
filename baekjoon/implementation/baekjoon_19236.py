import sys
import copy


def solution():
    sys.setrecursionlimit(10**6)
    grid, result = [], [0]
    for i in range(4):
        col = list(map(int, sys.stdin.readline().split()))
        tmp = []
        for j in range(4):
            k = 2*j
            tmp.append([col[k:k+2][0], col[k:k+2][1]-1])
        grid.append(tmp)

    dy, dx = (-1, -1, 0, 1, 1, 1, 0, -1), (0, -1, -1, -1, 0, 1, 1, 1)

    def find_fish(arr, src):
        for i in range(4):
            for j in range(4):
                if arr[i][j][0] == src:
                    return i, j
        return None

    def moving_fish(arr, y, x) -> None:
        for i in range(1, 17):
            pos = find_fish(arr, i)
            if pos is not None:
                fy, fx = pos
                fd = arr[fy][fx][1]
                for j in range(8):
                    nfy, nfx = fy + dy[fd], fx + dx[fd]
                    if -1 < nfy < 4 and -1 < nfx < 4:
                        if not (nfy == y and nfx == x):
                            arr[fy][fx][1] = fd
                            arr[nfy][nfx], arr[fy][fx] = arr[fy][fx], arr[nfy][nfx]
                            break
                    fd = (fd+1) % 8

    def eatable_fish(arr, y, x):
        pos = []
        sd = arr[y][x][1]
        nsy, nsx = y + dy[sd], x + dx[sd]  # 지속적으로 이동해야 하기 때문에 값이 누적 되도록 설계해야 한다.
        for i in range(4):
            if -1 < nsy < 4 and -1 < nsx < 4:
                if arr[nsy][nsx][0] != -1:
                    pos.append((nsy, nsx))
            y, x = nsy, nsx
        return pos

    def backtracking(arr, y, x, total):
        arr = copy.deepcopy(arr)
        total += arr[y][x][0]
        arr[y][x][0] = -1
        moving_fish(arr, y, x)
        position = eatable_fish(arr, y, x)
        if not len(position):
            result[0] = max(result[0], total)
            return

        for i, j in position:
            backtracking(arr, i, j, total)

    backtracking(grid, 0, 0, 0)
    print(result[0])


if __name__ == "__main__":
    solution()
