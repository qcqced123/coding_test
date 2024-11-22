import sys
from itertools import combinations


def solution():
    """ 원소: 팀 시너지, 대칭 아님 주의!!, 두 팀의 능력치 차이 "최소"
    idea: backtracking
        - overlapping 구조가 전혀 없음
        - sub-optimal 구조도 전혀 없음
        - 입력도 매우 작음
        - 사실 조합 아닐까...?
    1) 인자 정의
    2) 스택 호출 조건
    3) 스택 종료 조건
    """
    # init the data structure
    INF = sys.maxsize
    input = sys.stdin.readline
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    combs = list(combinations(list(range(N)), N//2))

    # find the global optimal solution
    answer = INF
    for i in range(len(combs)//2):
        team_start, team_link = 0, 0
        for j in range(len(combs[i])):
            for k in range(j+1, len(combs[i])):
                start_A, start_B = combs[i][j], combs[i][k]
                link_A, link_B = combs[-1-i][j], combs[-1-i][k]  # 지금 링크 팀 계산이 이상함
                team_start += grid[start_A][start_B] + grid[start_B][start_A]
                team_link += grid[link_A][link_B] + grid[link_B][link_A]

        answer = min(answer, abs(team_start - team_link))

    print(answer)


if __name__ == "__main__":
    solution()
