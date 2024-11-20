import sys


def solution():
    """ 스도쿠 완성하기
    idea: backtracking
        - 스택 종료 조건:
            - 정답 경우의 수를 찾거나
            - 더 이상, 스도쿠를 진행할 수 없는 경우
        - 스택 호출 조건:
            - 현재 칸에 숫자를 나열할 수 있을 때
        - 인자 정의:
            - 남은 노드들 리스트 (인덱스)
    1) 초기화 필요한 노드 위치 리스트 만들기
    2) 9개 영역에 대한 visited 배열 만들기
    3) backtracking 본판 만들기
    """
    # backtracking func
    sys.setrecursionlimit(10**6)

    def answering(arr: list[list]) -> None:
        for i in range(9):
            print(*arr[i], end='\n')

    def backtracking(arr: list) -> None:
        if not arr:
            answering(grid)
            exit()

        y, x = arr[0]
        dy, dx = y // 3, x // 3
        for num in range(1, 10):
            # 가로, 세로 체크
            if num not in row[y] and num not in column[x] and num not in diagonal[dy][dx]:
                grid[y][x] = num
                row[y].add(num), column[x].add(num), diagonal[dy][dx].add(num)
                backtracking(arr[1:])
                grid[y][x] = 0
                row[y].remove(num), column[x].remove(num), diagonal[dy][dx].remove(num)

    # init the data structure
    input = sys.stdin.readline
    row = [set() for _ in range(9)]
    column = [set() for _ in range(9)]
    diagonal = [[set() for _ in range(3)] for _ in range(3)]
    grid = [list(map(int, input().split())) for _ in range(9)]

    init_point = []
    for i in range(9):
        for j in range(9):
            if not grid[i][j]:
                init_point.append((i,j))

            else:
                cnt = grid[i][j]
                row[i].add(cnt), column[j].add(cnt), diagonal[i//3][j//3].add(cnt)

    # do the backtracking
    backtracking(init_point)


if __name__ == "__main__":
    solution()
