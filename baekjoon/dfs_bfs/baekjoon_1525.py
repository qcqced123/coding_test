import sys
from copy import deepcopy


def solution():
    """
    idea: backtrack
        - 최소 이동, 주어진 상태 만들기
        - 메모리 제한이 매우 타이트, pruning 활용한 optimization 필수
        - 스택 호출: curr의 다음 위치 값 중에서, result에서 현재 위치 값과 같은 방향을 찾는 경우만
            - if -1 < ny < 3 and -1 < nx < 3 and curr[ny][nx] == result[y][x]:

        - 스택 종료: prev == result
        - 인자 정의: 그리드(깊은 복사 필요)

    question:
        - 17% 틀림

    feedback:
        - 아놔, 문제를 거꾸로 풀었네, 초기 상태랑 목표 상태를 반대로 두고 풀었어
        - 스택 호출 조건 자체가 틀림
            - 진짜 다 세어 봐야 하는 것인가...

    reference:
        - https://www.acmicpc.net/board/view/19700
    """
    # backtrack func
    sys.setrecursionlimit(10**6)
    def backtrack(prev: list[list[int]], y: int, x: int, count: int):
        if prev[y][x] == result[y][x]:
            answer[0] = min(answer[0], count)
            return

        # call the next stack frame
        curr = deepcopy(prev)
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if -1 < ny < 3 and -1 < nx < 3 and curr[ny][nx] == result[y][x]:
                curr[y][x], curr[ny][nx] = curr[ny][nx], 0
                if count+1 < answer[0]:
                    backtrack(curr, ny, nx, count+1)
        return

    # get input data
    INF = sys.maxsize
    input = sys.stdin.readline
    result = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0],
    ]
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    grid = [list(map(int,input().split())) for _ in range(3)]

    # find the starting point
    sy = None
    sx = None
    for i in range(3):
        for j in range(3):
            if not grid[i][j]:
                sy = i
                sx = j
                break

    # start backtracking
    answer = [INF]
    backtrack(grid, sy, sx, 0)
    print(answer[0] if answer[0] != INF else -1)


def solution2():
    """
    idea: backtracking
        - 인자 정의: 그리드, 현재 위치, 이동 횟수
        - 호출 조건: 이동 횟수 < 최적값
        - 종료 조건: 이동 횟수 >= 최적값 or 그리드 == 목표 상태

    feedback:
        - 현재 스택의 그리드 상태를 1차원 문자열로 만들고, 그것을 visited로 활용!
    """
    # backtrack func
    def is_same(curr: list[list]):
        flag = 0
        for i in range(3):
            for j in range(3):
                if curr[i][j] != result[i][j]:
                    flag += 1
                    break

            if flag:
                break

        else:
            return 1

        return 0

    sys.setrecursionlimit(10**4)
    def backtracking(prev: list[list], y: int, x: int, count: int, path: str):
        nonlocal answer
        if is_same(prev):
            answer = min(answer, count)
            return

        curr = deepcopy(prev)
        for i in range(4):
            ny, nx, nc = y + dy[i], x + dx[i], count + 1
            if -1 < ny < 3 and -1 < nx < 3 and nc < answer:
                np = path + str(grid[ny][nx])
                if np not in visited:
                    curr[y][x], curr[ny][nx] = curr[ny][nx], 0
                    backtracking(curr, ny, nx, nc, np)
                    curr[y][x], curr[ny][nx] = 0, curr[ny][nx]  # for backtracking

        return

    # get input data
    INF = sys.maxsize
    input = sys.stdin.readline
    result = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0],
    ]
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    grid = [list(map(int, input().split())) for _ in range(3)]

    # find the starting point
    sy = None
    sx = None
    for i in range(3):
        for j in range(3):
            if not grid[i][j]:
                sy = i
                sx = j
                break

    # do backtrack
    answer = INF
    visited = set()
    src = str(grid[sy][sx])
    visited.add(src)
    backtracking(grid, sy, sx, 0, src)
    print(answer if answer != INF else -1)

    return


def solution3():
    """
    idea: bfs with hash structure
        - queue[i]: 그리드 상태
        - visited[i]: 이미 겪어본 그리드 상태

    reference:
        - https://www.acmicpc.net/board/view/47368
    """
    from collections import deque

    # bfs func
    def bfs(src: str):
        visited = set()
        visited.add(src)
        q = deque([(src, 0)])
        while q:
            vs, vc = q.popleft()
            pos = vs.find("0")
            vy, vx = divmod(pos, 3)

            for i in range(4):
                ny, nx = vy + dy[i], vx + dx[i]
                if -1 < ny < 3 and -1 < nx < 3:
                    ns = list(vs)
                    ns[3*ny+nx], ns[3*vy+vx] = ns[3*vy+vx], ns[3*ny+nx]
                    ns = "".join(ns)

                    if ns == result:
                        return vc + 1

                    if ns not in visited:
                        q.append((ns, vc+1))
                        visited.add(ns)
        return -1

    # get input datas
    input = sys.stdin.readline
    result = "123456780"
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    grid = [list(map(int, input().split())) for _ in range(3)]

    # do bfs
    src = ""
    for i in range(3):
        src += "".join(map(str, grid[i]))

    answer = bfs(src) if src != result else 0
    print(answer)


if __name__ == "__main__":
    solution3()
