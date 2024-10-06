import sys
from collections import deque


def solution():
    """ 상하좌우, 최대 문서 개수

    Question 1.
        래퍼런스 반례에 따르면, 그리드 탐색 시작 자체를 여러번 해야 되는데, 그걸 어떻게 코딩하지...........

    reference:
        https://www.acmicpc.net/board/view/141098
    """
    def update_grid(r: int, c: int) -> None:
        grid[r][c] = '.'
        return

    def is_valid_val(x: str, r: int = None, c: int = None) -> int:
        flag = 0
        if x == '.':
            flag += 1

        elif x.isupper():  # 가진 열쇠랑 대조
            if x.lower() in key_list:
                flag += 1
                update_grid(r, c)

        elif x.islower():  # 열쇠 리스트에 넣기
            flag += 1
            key_list.add(x)
            visited.clear()
            update_grid(r, c)

        elif x == '$':  # 결과에 추가
            flag += 1
            answer[0] += 1
            visited.clear()
            update_grid(r, c)

        return flag

    def bfs(y: int, x: int):
        def is_valid_pos() -> bool:
            """ function for validating the current key and door """
            return -1 < ny < R and -1 < nx < C and (ny, nx) not in visited

        q = deque([(y, x)])
        visited.add((y, x))
        while q:
            vy, vx = q.popleft()
            for i in range(4):
                ny, nx = dy[i] + vy, dx[i] + vx
                if is_valid_pos() and is_valid_val(grid[ny][nx], ny, nx):
                    # if not grid[ny][nx].isupper():
                    visited.add((ny, nx))
                    q.append((ny, nx))

        return

    input = sys.stdin.readline
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)

    for _ in range(int(input())):
        answer = [0]
        visited = set()
        R, C = map(int, input().split())
        grid = [list(input().rstrip()) for _ in range(R)]

        # get the validated starting point of current grid
        src_list = set()
        key_input = input().rstrip()
        key_list = set() if key_input == "0" else set(key_input)

        for y in range(R):
            for x in range(C):
                if not y or y == R-1 or not x or x == C-1:
                    cnt = grid[y][x]
                    if is_valid_val(cnt, y, x):
                        src_list.add((y, x))
        print(src_list)
        print(key_list)
        # preprocess for no entrance
        if not src_list:
            print(0)
            return

        # do search for document
        for src in src_list:
            src_y, src_x = src
            bfs(src_y, src_x)

        print(answer[0], end='\n')


if __name__ == "__main__":
    solution()
