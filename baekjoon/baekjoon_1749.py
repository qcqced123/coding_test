import sys


def solution():
    """
    idea: prefix sum with backtracking
        - 2차원 테이블 누적합 응용
        - 누적합 테이블 초기화
        - 가능한 쿼리 조합을 모두 구하기
        - 조합별 계산 하면서 최대값 갱신

    feedback:
        - 좌표 조합 방식이 N**4만 생각나서 pypy3으로 해결
        - gpt 물어 보니까 kadane 알고리즘이라는게 있음
            - 근데 저건 그냥 부분합 구하는 방식부터 최적화하는거라 일단 건너 뛰자
    """
    # helper func
    def calculate(y1, x1, y2, x2) -> int:
        return prefix[y2][x2] - prefix[y1-1][x2] - prefix[y2][x1-1] + prefix[y1-1][x1-1]

    # init data structure
    INF = sys.maxsize
    input = sys.stdin.readline
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    prefix = [[0]*(M+1) for _ in range(N+1)]

    # init prefix table
    for i in range(1, N+1):
        for j in range(1, M+1):
            prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + grid[i-1][j-1]

    # update the answer value with combinations
    # optimizing point
    answer = -INF
    for ly in range(1, N+1):
        for lx in range(1, M+1):
            for ry in range(ly, N+1):
                for rx in range(lx, M+1):
                    answer = max(answer, calculate(ly,lx,ry,rx))
    print(answer)


def solution2():
    def kadane(arr):
        max_current = max_global = arr[0]
        for x in arr[1:]:
            max_current = max(x, max_current + x)
            max_global = max(max_global, max_current)
        return max_global

    input = sys.stdin.readline
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    answer = -sys.maxsize

    for left in range(M):
        temp = [0] * N
        for right in range(left, M):
            for row in range(N):
                temp[row] += grid[row][right]
            answer = max(answer, kadane(temp))

    print(answer)


if __name__ == "__main__":
    solution()
