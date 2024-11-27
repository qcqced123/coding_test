import sys
from itertools import combinations


def solution():
    """
    idea: backtracking (combinations)
    """
    # get input
    INF = sys.maxsize
    input = sys.stdin.readline
    N = int(input())
    players = {i for i in range(N)}
    grid = [list(map(int, input().split())) for _ in range(N)]

    # make the case of squad
    answer = INF
    for i in range(1, N//2+1):
        for comb in combinations(range(N), i):
            # make the case of each team
            team_link = set(comb)
            team_start = players.difference(team_link)

            # calculate the team link
            link_overall = 0
            team_link = list(team_link)
            for j in range(len(team_link)-1):
                player_1 = team_link[j]
                for k in range(j+1, len(team_link)):
                    player_2 = team_link[k]
                    link_overall += grid[player_1][player_2] + grid[player_2][player_1]

            # calculate the team start
            start_overall = 0
            team_start = list(team_start)
            for j in range(len(team_start)-1):
                player_1 = team_start[j]
                for k in range(j + 1, len(team_start)):
                    player_2 = team_start[k]
                    start_overall += grid[player_1][player_2] + grid[player_2][player_1]

            answer = min(answer, abs(link_overall-start_overall))

    print(answer)


if __name__ == "__main__":
    solution()
