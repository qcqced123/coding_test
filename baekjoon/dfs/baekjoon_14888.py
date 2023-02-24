from itertools import permutations, product
import sys
"""
[풀이 시간]
14:05 ~ 14: 35

[변수 설명]
N => N개의 수로 이뤄진 수열
N-1 => N-1개로 이뤄진 연산자, 사칙 연산

[규칙]
1) 주어진 수의 순서 변경 불가
2) 식의 연산은 연산자 우선 순위 없이 앞에서부터 진행
3) 나눗셈의 경우 정수 몫만 취함
4) 음수를 양수로 임시로 바꿔 몫을 구한 뒤, 해당 몫을 다시 음수로 변환

[목표]
1) 주어진 수열, 연산자로 구할 수 있는 연산 최대값, 최소값 찾기
2) 따라서 입력 받은 연산자 개수 정보를 활용해 여러 연산자 세트를 만들어 준다
=> permutations 사용!
"""

# Input
N = int(input())
num_list = list(map(int, sys.stdin.readline().split()))
operator_count = list(map(int, sys.stdin.readline().split())) # add, subtract, product, divide
operator = ['+', '-', '*', '/'] # 연산자

# 연산자 세트 만들기 => product 사용
# Time Complexity => O(N)
operator_list = []
for idx, value in enumerate(operator_count):
    while value != 0:
        operator_list.append(operator[idx])
        value -= 1
operator_group = list(set(list(permutations(operator_list, N-1)))) # 연산자 세트, 중복 제거!

# 연산자 세트 별로 계산해서 결과 비교하기
result = [] # 개별 연산자 세트에 대한 결과 저장
for group in operator_group:
    temp_result = 0  # 중간 연산 결과 저장
    for idx, value in enumerate(num_list):
        # 첫 번째 항 예외처리
        if idx == 0:
            temp_result += value
            continue

        # 연산자에 따라 케이스 분류
        if group[idx-1] == '+':
            temp_result = temp_result + value
        if group[idx-1] == '-':
            temp_result = temp_result - value
        if group[idx-1] == '*':
            temp_result = temp_result * value
        if group[idx-1] == '/':
            # 음수인 경우 예외처리
            if temp_result < 0:
                temp_result = -int(-temp_result / value)
            if temp_result >= 0:
                temp_result = int(temp_result / value)

    result.append(temp_result)

print(max(result)) # 최대값 출력
print(min(result)) # 최소값 출력
