import sys


def solution():
    """
    idea: prefix sum
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

    # case 1


if __name__ == "__main__":
    solution()
