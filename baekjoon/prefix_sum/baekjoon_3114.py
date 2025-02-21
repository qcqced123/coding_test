import sys


def solution():
    """
    idea: prefix sum + dynamic programming
        - 2D prefix sum
        - dp[i][j][k]:
            - i == row
            - j == col
            - k == prev direction

    limit: N^2 * logN
    """
    # helper func
    def calculate(y2: int, x2: int, y1: int, x1: int,  v: int):
        return prefix[y2][x2][v] - prefix[y2][x1-1][v] - prefix[y1-1][x2][v] + prefix[y1-1][x1-1][v]


    # get input data
    input = sys.stdin.readline
    R, C = map(int, input().split())
    grid = [list(map(str, input().split())) for _ in range(R)]

    # init and update the 2D table prefix sum
    prefix = [[[0, 0] for _ in range(C+1)] for _ in range(R+1)]
    for i in range(1, R+1):
        for j in range(1, C+1):
            curr = grid[i-1][j-1]
            cnt_apple, cnt_banana = 0, 0
            if curr[0] == "A": cnt_apple += int(curr[1:])
            else: cnt_banana += int(curr[1:])  # 숫자 문자열 to 숫자 캐스팅할 때 자리수 조심하자!

            # caching for apple, banana tree
            prefix[i][j][0] = prefix[i-1][j][0] + prefix[i][j-1][0] - prefix[i-1][j-1][0] + cnt_apple
            prefix[i][j][1] = prefix[i-1][j][1] + prefix[i][j-1][1] - prefix[i-1][j-1][1] + cnt_banana

    # init and update the dp cache
    dp = [[[0]*3 for _ in range(C+1)] for _ in range(R+1)]
    for i in range(1, R+1):
        for j in range(1, C+1):
            dp[i][j][0] = max(dp[i-1][j-1]) + calculate(R,j,i+1,j,0) + calculate(i,C,i,j+1,1)  # from diagonal direction
            dp[i][j][1] = max(dp[i][j-1]) - calculate(i,j,i,j,1) + calculate(R,j,i+1,j,0)  # from left element
            dp[i][j][2] = max(dp[i-1][j]) - calculate(i,j,i,j,0) + calculate(i,C,i,j+1,1)

    # answering the question
    print(max(dp[-1][-1]))


if __name__ == "__main__":
    solution()
