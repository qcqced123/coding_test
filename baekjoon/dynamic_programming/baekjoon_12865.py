import sys
"""
[풀이 시간]
1) 17:40 ~ 18:25

[요약]
1) 여행에 필요한 물건 N개, 무게 W, 가치 V, 배낭 무게는 최대 K
    - 최대 무게 K를 넘기지 않고 최대한 많은 가치를 배낭에 담기
    -
[전략]
1) 이중 루프 가능한 문제
2) 최대한 많은 가치를 제한된 무게 안에 넣기
    - Greedy 혹은 Dynamic Programming 방식 적용 필요
    - 어차피 물건의 무게가 K보다 크다면 의미가 없기 때문에, 무게를 기준으로 오름 차순 정렬
    - 모든 경우의 수에 대한 판단 & 비교 필요함 => DP Table 방식 적용 필요
"""
N, K = map(int, sys.stdin.readline().split())
item_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
item_list.sort(key=lambda x: x[0])
value_table = [[[0, 0] for _ in range(N)] for _ in range(N)]
max_value = 0
for i in range(N):
    for j in range(N):
        if i == j:
            value_table[i][j] = item_list[i]
            continue
        if j == 0:
            value_table[i][j] = value_table[j][i]
            continue

        if value_table[i][j-1][0] + item_list[j][0] <= K:
            """ 이전 물건 + 현재 물건을 배낭에 담는 케이스 """
            if value_table[i][j-1][1] >= value_table[i][j-1][1] + item_list[j][1]:
                tmp_weight = value_table[i][j-1][0]
                tmp_value = value_table[i][j-1][1]
            else:
                tmp_weight = value_table[i][j-1][0] + item_list[j][0]
                tmp_value = value_table[i][j-1][1] + item_list[j][1]

            value_table[i][j] = [tmp_weight, tmp_value]
            max_value = max(max_value, tmp_value)
print(max_value)
