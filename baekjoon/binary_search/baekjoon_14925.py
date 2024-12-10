import sys


def solution():
    """
    idea: prefix sum
        - 2차원 테이블 누적합
        - 올바른 영역 판단 기준: 누적합 이용
            - 현재 영역의 누적합 == 0, 올바른 영역
            - 현재 영역의 누적합 > 0, 잘못된 영역
    question:
        - 아마 테스트 케이스 중에서 최악의 경우는 없는거 같은데, 잘못하면 1000^3이라서 시간 초과 당함
    """
    def calculate(y1, x1, y2, x2) -> int:
        cnt = prefix[y2+1][x2+1] - prefix[y1][x2+1] - prefix[y2+1][x1] + prefix[y1][x1]
        return 1 if not cnt else 0

    input = sys.stdin.readline
    M, N = map(int, input().split())
    prefix = [[0]*(N+1) for _ in range(M+1)]
    grid = [list(map(int, input().split())) for _ in range(M)]

    # init prefix sum table
    for i in range(1, M+1):
        for j in range(1, N+1):
            prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + grid[i-1][j-1]

    # check validation of current area of square
    answer = 0
    for s in range(1, min(M,N)+1):
        flag = 0
        for i in range(M):
            for j in range(N):
                y1, x1 = i, j
                y2, x2 = i+s-1, j+s-1
                if -1 < y2 < M and -1 < x2 < N and calculate(y1, x1, y2, x2):
                    flag += 1
                    answer = s
                    break
            if flag:
                break

        if not flag:
            break

    print(answer)


if __name__ == "__main__":
    solution()
