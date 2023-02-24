import sys
"""
[풀이 시간]
1) 16:30 ~ 17:00

[규칙]
1) G : 공항 게이트 개수
2) P : 공항 도착 예정 비행기 개수
3) i : 도킹 하려는 비행기
=> 이번 시점 비행기가 어느 게이트에도 도킹을 못하면, 공항 폐쇄, 이후 시점에 도착하는 모든 항공기 도착 X
=> 최대 도킹 가능한 비행기
[전략]
- 일단 시간 압박이 심한 문제, 무조건 Local Optimal Sol을 찾아야 함
- 시점이 중요해서 비행기 스케줄을 정렬 못함
- 근데 생각해보면 줄 수 있는 게이트 숫자 중에서 가장 큰 번호를 줘야 하지 않을까?? 이것도 계단식 논같은 경우가 되는 거니까
- 저렇게 풀면 O(n^2)이 되는구나
- 포트 번호 == 사용 가능한 포트 수 
"""
# Input
gate_list, checker, count, result = [False] * (int(sys.stdin.readline()) + 1), True, 0, 0 # index 맞추기
for _ in range(int(sys.stdin.readline())):
    max_num = int(sys.stdin.readline())

    while checker:
        if max_num == 0:
            checker = False
            break

        if not gate_list[max_num]:
            gate_list[max_num] = True  # 도킹 성공
            result += 1
            break
        # 도킹 가능한 곳을 찾아서...
        max_num -= 1

    if not checker:
        break

print(result)

