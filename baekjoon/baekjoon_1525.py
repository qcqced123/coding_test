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
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0],
    ]
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    result = [list(map(int,input().split())) for _ in range(3)]

    # start backtracking
    answer = [INF]
    backtrack(grid, 2,2, 0)
    print(answer[0] if answer[0] != INF else -1)


if __name__ == "__main__":
    solution()
