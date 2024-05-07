import sys
from typing import List


def my_solution():
    """
    1) 종료 조건 설정에 유의해서 문제 풀어보자
    """
    N = int(sys.stdin.readline())
    grid = [[0]*N for _ in range(N)]

    answer = [0]
    sys.setrecursionlimit(10**4)

    def row_valid(curr_y: int, curr_x: int) -> bool:
        for row in range(curr_y):
            if grid[row][curr_x]: return False
        return True

    def left_diagaonal_valid(curr_y: int, curr_x: int) -> bool:
        y, x = curr_y, curr_x
        while -1 < y < curr_y and -1 < x < curr_x:
            if grid[y][x]: return False
            y -= 1
            x -= 1
        return True

    def right_diagaonal_valid(curr_y: int, curr_x: int) -> bool:
        y, x = curr_y, curr_x
        while -1 < y < curr_y and curr_x < x < N:
            if grid[y][x]: return False
            y -= 1
            x += 1

        return True

    def backtracking(row: int):
        if row == N:
            answer[0] += 1
            return

        for i in range(N):
            if row_valid(row, i) and left_diagaonal_valid(row, i) and right_diagaonal_valid(row, i):
                grid[row][i] = 1
                backtracking(row+1)
                grid[row][i] = 0

    backtracking(0)
    return answer[0]


def solution(N: int) -> int:
    def get_answer(n: int, y: int, width: List, diagonal1: List, diagonal2: List):
        answer = 0
        if y == n:
            answer += 1
        else:
            for i in range(n):
                if width[i] or diagonal1[i + y] or diagonal2[i - y + n]:
                    continue
                width[i] = diagonal1[i + y] = diagonal2[i - y + n] = True
                answer += get_answer(n, y+1, width, diagonal1, diagonal2)
                width[i] = diagonal1[i + y] = diagonal2[i - y + n] = False
        return answer
    result = get_answer(N, 0, [0]*N, [0]*(2*N), [0]*(2*N))
    return result

if __name__ == "__main__":
    my_solution()
