import sys


def solution():
    """
    idea: prefix sum with brute force
        - 2차원 테이블 부분합 변형
        - 2차원 부분합 테이블 초기화
        - 경우의 수를 어떻게 잡을까?? 조합??

    question:
        - 직사각형 3개로 나누는 방법을 모르겠음

    feedback:
        - 최대 6가지 경우만 존재, 그거 죄다 하드 코딩

    """
    # helper func
    def calculate(y1, x1, y2, x2):
        return prefix[y2+1][x2+1] - prefix[y1][x2+1] - prefix[y2+1][x1] + prefix[y1][x1]

    # get input
    input = sys.stdin.readline
    N, M = map(int, input().split())
    grid = [list(map(int, list(input().rstrip()))) for _ in range(N)]

    # init prefix sum table
    prefix = [[0]*(M+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, M+1):
            prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + grid[i-1][j-1]

    # case 1: 가로 방향 분할
    answer = 0
    fy1, fx1 = 0, 0  # 첫번째 직사각형 왼쪽 모서리 시작 위치
    ty2, tx2 = N-1, M-1  # 세번째 직사각형 오른쪽 모서리 끝 위치
    for i in range(N-2):  # 첫번째 직사각형 오른쪽 모서리 루프
        fy2, fx2 = i, M-1
        first = calculate(fy1, fx1, fy2, fx2)
        for j in range(i, N-1):  # 두번째 직사각형 오른쪽 모서리 루프, 세번째 직사각형 왼쪽 모서리 루프
            second = calculate(fy2+1, 0, j, 0)
            third = calculate(j+1, 0, ty2, tx2)
            answer = max(answer, first*second*third)

    # case 2: 세로 방향 분할
    for i in range(M-2):
        fy2, fx2 = N-1, i
        first = calculate(fy1, fx1, fy2, fx2)
        for j in range(i, M-1):
            second = calculate(0, fx2+1, N-1, j)
            third = calculate(0, j+1, N-1, M-1)
            answer = max(answer, first * second * third)

    # case 3
    for i in range(N-1):
        fy2, fx2 = i, M-1
        first = calculate(fy1, fx1, fy2, fx2)
        for j in range(M-1):
            second = calculate(i+1, 0, N-1, j)
            third = calculate(i+1, j+1, N-1, M-1)
            answer = max(answer, first * second * third)

    # case 4
    for i in range(N-1, 0, -1):
        fy1, fx1 = i, 0
        fy2, fx2 = N-1, M-1
        first = calculate(fy1, fx1, fy2, fx2)
        for j in range(M-1):
            second = calculate(0, 0, i-1, j)
            third = calculate(0, j+1, i-1, M-1)
            answer = max(answer, first * second * third)

    # case 5
    for i in range(M-1):
        fy1, fx1 = 0, 0  # this position must be pinned at (0,0)
        fy2, fx2 = N-1, i
        first = calculate(fy1, fx1, fy2, fx2)
        for j in range(N-1):
            second = calculate(0, i+1, j, M-1)
            third = calculate(j+1, i+1, ty2, tx2)
            answer = max(answer, first * second * third)

    # case 6
    for i in range(M-1, 0, -1):
        fy1, fx1 = 0, i
        fy2, fx2 = N-1, M-1
        first = calculate(fy1, fx1, fy2, fx2)
        for j in range(N-1):
            second = calculate(0, 0, j, i-1)
            third = calculate(j+1, 0, N-1, i-1)
            answer = max(answer, first * second * third)

    print(answer)


if __name__ == "__main__":
    solution()
