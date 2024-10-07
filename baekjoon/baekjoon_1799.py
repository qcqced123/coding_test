import sys


def solution():
    """ 체스 비숍 구현
    condition:
        1) 색칠 위치 못 놓음: 원소값 0
        2) N-비숍 비슷한 문제

    idea: back tracking
        1) call stack 기준:
            - 비숍을 놓았을 때

        2) end stack 기준:
            - 더 이상 비숍을 못 놓는 상황
            - 현재 스택 프레임 값으로 answer 값 최신화

        3) recursive 내부 디자인
            - 비숍 못 놓는 위치 업데이트
            - 다음 비숍 놓을 수 있는 위치 찾기
            - 놓을 수 있는 위치 찾으면 다음 스택 호출
            - 그리드를 복사해버리면 참 편할텐데,,,,,
    point:
        1) 효율적인 대각선 탐색: linear로 줄이기
            - 원래 초창기부터 0이었던 애들은 계속 0으로 둬야 되는데, 내 코드에서는 얘네가 1로 바뀌네
            - 이게 해결 가능함?
    """
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    # get input
    answer = [0]
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    # function for updating grid for non-movable
    def update_grid(y: int, x: int, mode: str):
        value = 0 if mode == 'update' else 1
        for i in range(N):
            # lower right, upper left diagonal
            if y+i < N:
                if x+i < N:
                    grid[y+i][x+i] = value  # lower right diagonal

                if x-i > -1:
                    grid[y+i][x-i] = value  # lower left diagonal

            if y-i > -1:
                if x-i > -1:
                    grid[y-i][x-i] = value  # upper left diagonal

                if x+i < N:
                    grid[y-i][x+i] = value  # upper right diagonal

        grid[y][x] = 2 if mode == 'update' else 1

    def backtracking(y: int, x: int, count: int) -> None:
        # update the not movable area of bishop
        update_grid(y, x, "update")
        answer[0] = max(answer[0], count)

        if x == N-1:
            y += 1
            x -= N

        for ny in range(y, N):
            for nx in range(x+1, N):
                if grid[ny][nx] == 1:
                    backtracking(ny, nx, count+1)
                    update_grid(ny, nx, "revert")

    for r in range(N):
        for c in range(N):
            if grid[r][c] == 1:
                backtracking(r, c, 1)

    print(answer[0])


if __name__ == "__main__":
    solution()
