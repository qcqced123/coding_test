import sys
"""
[풀이 시간]
1) 21:50 ~ 22:30

[문제 정리]
1) 하루 한 명씩 상담, 서로 다른 사람
2) T: 상담 소요 시간(일수), P: 상담 금액, N = 남은 근무 날짜

[전략]
1) Recursive Call & DFS 사용
"""


def dfs(day, tmp_cost):
    if day >= N:
        return
    period, cost = schedule_list[day][0], schedule_list[day][1]
    left_day = N - day + 1
    if period <= left_day:
        tmp_cost += cost
        dfs(day + period, tmp_cost)
    else:
        tmp_left_day = N - day + 2
        if schedule_list[day+1][0] <= tmp_left_day:
            dfs(day+1, tmp_cost)
    return


N = int(sys.stdin.readline())
schedule_list, max_money = [[0, 0]], 0
for i in range(1, N+1):
    schedule_list.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N+1):
    current_cost = 0
    dfs(i, current_cost)
    max_money = max(max_money, money)
print(max_money)
