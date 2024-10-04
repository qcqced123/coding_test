import sys


def solution():
    """ 스도쿠 게임, (N-Queens 심화)
    condition:
        1) 3x3에 1~9 중복 X
        2) 가로, 세로에 1~9 중복 X
        => 원소값 == 0 인 애들 채워넣기

    idea: backtracking
        1) 가로 체크 로직
        2) 세로 체크 로직
        3) 3x3 영역 체크 로직

    optimization point:
        1) deepcopy 대신 값 되돌리기
        2) is_valid 로직 변경: 배열 순회 대신, 세트 사용

    000000000
    000000000
    000000000
    000000000
    000000000
    000000000
    000000000
    000000000
    000000000
    """
    def set_value(y: int, x: int, v: int):
        arr[y][x] = v
        row_check[y].add(v)
        col_check[x].add(v)
        square_check[y//3][x//3].add(v)
        return

    def del_value(y: int, x: int, v: int):
        arr[y][x] = 0
        row_check[y].remove(v)
        col_check[x].remove(v)
        square_check[y // 3][x // 3].remove(v)  # good point
        return

    def is_valid(y: int, x: int, v: int) -> int:
        return v not in row_check[y] and v not in col_check[x] and v not in square_check[y//3][x//3]

    def backtrack(y: int, x: int):
        if y == 8 and x == 8:
            for i in range(1, 10):
                if is_valid(8, 8, i):
                    arr[y][x] = i
                    break

            # check grid logic
            for i in range(len(arr)):
                print("".join(map(str, arr[i])), end='\n')

            exit()

        next_y, next_x = (y + (x + 1) // 9, (x + 1) % 9)
        if arr[y][x]:
            backtrack(next_y, next_x)

        else:
            for i in range(1, 10):
                if is_valid(y, x, i):
                    set_value(y, x, i)
                    backtrack(next_y, next_x)
                    del_value(y, x, i)
        return

    sys.setrecursionlimit(10**4)
    arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(9)]

    row_check = [set() for _ in range(9)]
    col_check = [set() for _ in range(9)]
    square_check = [[set() for _ in range(3)] for _ in range(3)]

    for r in range(9):
        for c in range(9):
            if arr[r][c]:
                set_value(r, c, arr[r][c])

    backtrack(0, 0)


if __name__ == "__main__":
    solution()
