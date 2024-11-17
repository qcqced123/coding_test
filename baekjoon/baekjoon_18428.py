import sys


def solution():
    """
    idea: backtracking
        - 인자 정의: 남은 장애물 숫자
        - 스택 종료 조건: 장애물 남은거 없을 때
            - 걸리는 학생수 카운트
            - answer = min(answer, count)
        - 스택 호출 조건: 장애물 놓기
            - deepcopy x, backtracking logic
    """
    # init the data structure
    INF = sys.maxsize
    input = sys.stdin.readline
    N = int(input())
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    grid = [list(map(str, input().split())) for _ in range(N)]
    teachers = [(i,j) for j in range(N) for i in range(N) if grid[i][j] == "T"]
    # backtracking func
    answer = INF
    sys.setrecursionlimit(10**6)
    def backtracking(remain: int) -> None:
        nonlocal answer
        if not remain:  # end point of stack call
            count = 0
            for ty, tx in teachers:
                for i in range(4):
                    for j in range(1, N):
                        nty, ntx = ty + dy[i]*j, tx + dx[i]*j
                        if not (-1 < nty < N and -1 < ntx < N) or grid[nty][ntx] == "O":
                            break

                        elif grid[nty][ntx] == "S":
                            count += 1
            if not count:
                print("YES")
                exit()

            return

        for y in range(N):
            for x in range(N):
                if grid[y][x] == "X":
                    grid[y][x] = "O"
                    backtracking(remain-1)
                    grid[y][x] = "X"

    backtracking(3)
    print("NO")


if __name__ == "__main__":
    solution()
