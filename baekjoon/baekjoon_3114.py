import sys
from collections import deque


def solution():
    """
    idea: prefix sum + dynamic programming
        [prefix sum]
        - 미리 전체 전역 정보를 알고 있어야 시간 제한 맞출 수 있지 않을까??
        - 전체 전역 정보를 미리 캐싱 해두고, 경로를 선택할 때마다 상수 시간에 업데이트 가능하도록
        - prefix[i][j] == 해당 칸까지 고려했을 떄, 바나나 & 사과 나무 개수

        [dynamic programming]
        - dp[i]:

    limit: N^2 * logN

    question:
        - 전역 정보를 상수 시간에 접근 가능 하도록 누적합을 떠올리고, 자료구조도 잘 잡았으나, 이후 탐색 과정을 어떻게 설계할지 전혀 감이 안옴
    """
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
            if curr[0] == "A": cnt_apple += int(curr[1])
            else: cnt_banana += int(curr[1])

            # caching for apple, banana tree
            prefix[i][j][0] = prefix[i-1][j][0] + prefix[i][j-1][0] - prefix[i-1][j-1][0] + cnt_apple
            prefix[i][j][1] = prefix[i-1][j][1] + prefix[i][j-1][1] - prefix[i-1][j-1][1] + cnt_banana

    # init and update the dp cache


    # check the current state of array
    for i in range(R+1):
        print(prefix[i], end="\n")


def solution2():
    """
    Args:
    """
    return


if __name__ == "__main__":
    solution()
