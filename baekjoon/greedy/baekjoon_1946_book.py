import sys

# Input
T = int(input())
N_list = []
answer = []
for i in range(T):
    N = int(input())
    temp_list = [list(map(int, sys.stdin.readline().split())) for col in range(N)]
    temp_list.sort()
    min_rank = temp_list[0][1]  # 1차 필기 기준 1등의 2차 면접 점수를 현재 가장 안좋은 면접 점수로 설정
    counter = 1
    for idx in range(N):
        rank = temp_list[idx][1]
        if rank < min_rank:  # 뒤에 오는 애들은 이미 1차 필기 점수가 낮기 때문에 익렇게 해줘야 조건에 성립
            min_rank = rank
            counter += 1
    answer.append(counter)

for i in answer:
    print(i)
