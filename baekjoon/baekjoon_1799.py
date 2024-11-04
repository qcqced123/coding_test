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
        2) 백트래킹 과정에서 원래 색칠된 영역의 값이 뒤바뀌는 문제 발생
            - 비숍의 공격에 의해서 갈 수 없는 공간의 원소는 '-1'
            - 기존 색칠된 영역에 의해서 갈 수 없는 공간의 원소는 '0'
            - 분기 컨디션에 위와 같은 조건 추가
            - 어차피 1이 아니면, 비숍을 못두게 만들어놨으니까 상관없음
        3) 백트래킹 과정에서 본인이 바꿨던 영역만 수정해야 되는데, 다른 영역도 바꿔버림
            - 그래서 무한루프 발생
            - 그냥 원소값을 중첩시키는 방법으로 가자

    reference:
        https://www.acmicpc.net/board/view/103135

    result:
        1) 시간 초과 발생 (8x8 이상)
    """
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    # get input
    answer = [0]
    N = int(input())

    grid = []
    src_point = []
    for i in range(N):
        col = list(map(int, input().split()))
        for j in range(len(col)):
            if col[j] == 1:
                src_point.append((i,j))
        grid.append(col)

    # helper function
    def is_valid(y: int, x: int):
        if grid[y][x] > 1:
            grid[y][x] = 1

    # function for updating grid for non-movable
    def update_grid(y: int, x: int, mode: str):
        value = -1 if mode == 'update' else 1  # for updating area of attacking by bishop
        for i in range(N):
            # lower right, upper left diagonal
            if y+i < N:
                if x+i < N and grid[y+i][x+i] < 2:
                    grid[y+i][x+i] += value  # lower right diagonal
                    is_valid(y+i, x+i)

                if x-i > -1 and grid[y+i][x-i] < 2:
                    grid[y+i][x-i] += value  # lower left diagonal
                    is_valid(y+i, x-i)

            if y-i > -1:
                if x-i > -1 and grid[y-i][x-i] < 2:
                    grid[y-i][x-i] += value  # upper left diagonal
                    is_valid(y-i, x-i)

                if x+i < N and grid[y-i][x+i] < 2:
                    grid[y-i][x+i] += value  # upper right diagonal
                    is_valid(y-i, x+i)

        grid[y][x] = 2 if mode == 'update' else 1

    def backtracking(y: int, x: int, count: int) -> None:
        # update the not movable area of bishop
        update_grid(y, x, "update")
        answer[0] = max(answer[0], count)

        # update index pointer
        row_pointer = y
        col_pointer = x
        if col_pointer == N-1:
            row_pointer += 1
            col_pointer = -1

        for ny in range(row_pointer, N):
            for nx in range(col_pointer+1, N):
                if grid[ny][nx] == 1:
                    backtracking(ny, nx, count+1)
                    update_grid(ny, nx, "revert")
            else:
                col_pointer = -1

    for i,j in src_point:
        backtracking(i, j, 1)

    print(answer[0])


def solution2():
    """
    idea: backtracking
        - 초기 색칠된 부분 처리 (비숍에 의해 갈 수 없는 공간이랑 구분 필요)
        - 인자 정의: 현위치, 비숍개수
        - 스택 종료: 더 이상 비숍 둘 곳 없을 떄
        - 스택 호출: 비숍을 어딘가에 뒀을 떄
        - 추가 기능: 비숍 공격 위치 찾기, 되돌리기
    """
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    N = int(input())
    grid = []
    src_point = []
    for i in range(N):
        col = list(map(int, input().split()))
        for j in range(len(col)):
            if col[j] == 1:
                src_point.append((i, j))
        grid.append(col)

    # backtracking func
    answer = 0
    def backtracking(remain: list, count: int) -> None:
        nonlocal answer
        if not remain:
            answer = max(answer, count)
            return

        for i in range(len(remain)):
            ny, nx = remain[i]
            if grid[ny][nx] != 1:
                continue

            grid[ny][nx] = 3
            cache = attack(ny, nx)  # for backtracking
            new_remain = remain[:i] + remain[i+1:]
            backtracking(new_remain, count+1)

            # revert attacked by bishop
            grid[ny][nx] = 1
            for vy, vx in cache:
                grid[vy][vx] = 1

    def attack(y: int, x: int) -> list:
        result = []
        rp, cp = abs(y-x), y+x
        for i in range(N):
            if 0 <= i + rp < N and grid[i][i+rp] == 1:
                grid[i][i+rp] = 2
                result.append((i, i+rp))

            elif 0 <= i + cp < N and grid[i][i+cp] == 1:
                grid[i][i+cp] = 2
                result.append((i, i+cp))

        return result

    backtracking(src_point, 1)
    return answer


if __name__ == "__main__":
    print(solution2())
