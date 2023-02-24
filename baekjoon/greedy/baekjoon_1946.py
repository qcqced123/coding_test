import sys

"""
[풀이 시간]
1) 13:00 ~ 13:40

[규칙]
1) 1차 서류 심사 & 2차 면접
2) 특정 지원자의 서류 점수, 면접 점수 중 하나라도 다른 지원자보다 높은 지원자만 뽑는다
=> 즉 

[변수]
T => 테스트 케이스 수
N => 개별 테스트 케이스의 지원자 숫자 (서류 등수, 면접 등수)

[아이디어]
1) 나머지 모든 지원자들과 일대일로 비교, 한 번이라도 둘 다 성적이 안좋으면 안된다는 의미
=> 5,5
=> 3,6/7,3//5,7/2,5
"""

# Input
T = int(input())
N_list = []
score_list = []
for i in range(T):
    temp_list = []
    N = int(input())
    N_list.append(N)
    for j in range(N):
        temp_list.append(list(map(int, sys.stdin.readline().split())))
    score_list.append(sorted(temp_list))

print(score_list)

# 지원자 일대일 비교
answer = []
for k, j in enumerate(N_list): # 상수 시간
    result_list = []
    for idx in range(j):
        # 예외 처리 => 현재 연산 대상 원소가 리스트의 마지막 원소
        if idx == j-1:
            continue
        for sub_idx in range(idx+1, j):
            if score_list[k][idx][0] > score_list[k][sub_idx][0] and score_list[k][idx][1] > score_list[k][sub_idx][1]:
                result_list.append((score_list[k][idx][0], score_list[k][idx][1]))
            if score_list[k][idx][0] < score_list[k][sub_idx][0] and score_list[k][idx][1] < score_list[k][sub_idx][1]:
                result_list.append((score_list[k][sub_idx][0], score_list[k][sub_idx][1]))
    answer.append(j - len(set(result_list)))

for i in answer:
    print(i)
