import sys
"""
[풀이 시간]
1) 20:20 ~ 21:00

[요약]
1) 양수, +, -, 괄호를 통해 수식 작성
    - 수식의 연산 결과가 최소가 되도록 괄호를 치자
[전략]
1) 시간 압박 적은 문제
2) 최소값 구하는 문제
    - 역시 Greedy, 정렬 대상 및 방법에 대한 고민 필요

"""
element_list, counter, checker, result, tmp = [element for element in sys.stdin.readline().rstrip()], 0, False, '', ''
for i in range(len(element_list)):
    if element_list[i] == '-' and counter == 0:
        element_list.insert(i+1, '(')
        counter += 1
        checker = True
    elif element_list[i] == '-' and counter == 1:
        element_list.insert(i-1, ')')
        counter = 0
        checker = False

if checker:
    element_list.append(')')

none_zero = 0
for i in range(len(element_list)):
    if element_list[i] == 0 and none_zero == 0:
        continue

    elif element_list[i] == 0 and none_zero != 0:
        result += element_list[i]

    if element_list[i] != 0:
        if element_list[i] == '+' or element_list[i] == '-' or element_list[i] == '(' or element_list[i] == ')':
            none_zero = 0
            result += element_list[i]
        else:
            none_zero += 1
            result += element_list[i]

print(eval(result))
# for i in range(len(element_list)):
#     """ let's count """
#     if element_list[i] != '-' and element_list[i] != '+' and element_list[i] != '(' and element_list[i] != ')':
#         tmp += element_list[i]
#     else:
#         if len(tmp) > 0:
#             tmp = str(int(tmp))
#         result += tmp + element_list[i]
#         tmp = ''
# result += tmp
# print(eval(result))
