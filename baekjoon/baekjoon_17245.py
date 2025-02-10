import sys


def solution():
    """
    idea: parametric search
        - 최적화 대상/범위: minimum minute, 1 to total
    """
    # helper func
    def calculate(curr: int) -> int:
        result = 0
        for i in range(N):
            for j in range(N):
                element = grid[i][j]
                if element < curr: result += element
                else: result += curr

        return result


    # get input
    input = sys.stdin.readline
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    # calculate the total computers
    answer = 0
    l, r, total = 1, 0, 0
    for i in range(N):
        for j in range(N):
            total += grid[i][j]
            r = max(r, grid[i][j])

    # do parametric search
    while l <= r:
        mid = (l+r) // 2  # current state of minute
        cnt = calculate(mid)
        if cnt >= (total / 2):
            answer = mid
            r = mid - 1

        else:
            l = mid + 1

    print(answer)

if __name__ == "__main__":
    solution()
