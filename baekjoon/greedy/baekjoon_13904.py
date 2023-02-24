import sys

"""
[풀이 시간]
1) 21:30 ~ 22:00

[변수]
1) N => 과제 개수
2) D => 과제 마감일까지 남은 일수
3) W => 과제 점수

[규칙]
1) 하루에 한 과제씩 끝낼 수 있음
2) 모든 과제 점수의 총합이 가장 높도록
3) 과제 개수가 최대 1000개라서 시간 압박은 크게 없을 것 같다

[아이디어]
1) 입력을 모두 받고 나서 조작
2) 남은 일수가 동일하게 남은 과제가 2개 이상 나올 때까지 루프 돌리기
=> 나온 경우: 남은 일수가 4일인데 총 과제가 6개라면 6개 중 4개 뽑아서 더한 값이 최대가 되도록 뽑자
=> 없는 경우: 쭉 보내다가 주어진 과제를 모두 탐색했을 때 모두 더함
"""

# Input
temp_list, result, count = [], 0, 0
assign_list = [list(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline()))]
assign_list = sorted(assign_list, key=lambda x: x[0]) # 오름차순 정렬

temp_list.append(assign_list[0][1]) # 첫번째 항 추가
# 남은 일수가 동일하게 남은 과제가 2개 이상 나올 때까지 루프 돌리기
for i in range(1, len(assign_list), 1):
    if assign_list[i-1][0] != assign_list[i][0]:
        # 마지막 항
        if i == len(assign_list) - 1:
            temp_list.append(assign_list[i][1])
            result += sum(temp_list)
            break
        else:
            temp_list.append(assign_list[i][1])
    else:
        # 마지막 항
        if i == len(assign_list) - 1:
            temp_list.append(assign_list[i][1])
            temp_list.sort(reverse=True)
            count = assign_list[i][0] - count
            result += sum(temp_list[0:count])
            break
        # 마지막 항이 아닌 경우
        elif assign_list[i][0] != assign_list[i+1][0]:
            temp_list.append(assign_list[i][1])
            temp_list.sort(reverse=True)
            count = assign_list[i][0] - count
            result += sum(temp_list[0:count])
            temp_list = [] # 리스트 초기화
        else:
            temp_list.append(assign_list[i][1])

print(result)