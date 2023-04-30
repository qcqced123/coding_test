import sys
"""
[풀이 시간]
1) 15:30 ~ 16:00

[전략]
1) 카드 개수를 최대 비용을 사용해 채우기
    - 같은 개수라면 비싼게 더 좋은 카드가 담겨있을 확률이 높다
    - 최대값: Greedy 혹은 DP
2) 주어진 Cost List의 인덱스가 곧 카드 개수를 의미
    - DP가 적합할 것으로 생각, 정렬이 불가능
    - 전형적인 Knapsack Problem으로 보인다.
"""
N = int(sys.stdin.readline())
cost_list = list(map(int, sys.stdin.readline().split()))
cost_table, max_cost = [[0] * (len(cost_list)+1) for _ in range(N+1)], 0  # cost_list index == cost_table row index

for i in range(1, len(cost_table)):
    """ row iterate """
    for j in range(1, len(cost_table[i])):
        num_card = i
        if i == 0 or j == 0:
            continue

        elif num_card <= j:
            cost_table[i][j] = max(cost_list[i-1] + cost_table[i][j - num_card], cost_table[i-1][j])  # 양쪽 비교가 맞음
            max_cost = max(max_cost, cost_table[i][j])

        else:
            cost_table[i][j] = max(cost_table[i][j-1], cost_table[i-1][j])  # 저렇게 양쪽을 모두 비교 하는게 맞다
            max_cost = max(max_cost, cost_table[i][j])
print(max_cost)
        
