import sys
from collections import deque
"""
[시간]
1) 18:25 ~ 18:55

[요약]
1) 새로운 언어 AC: AC는 정수 배열에 연산을 하기 위해 만든 언어
    - R(뒤집기): 배열에 있는 수의 순서를 뒤집는 함수 => reversed
    - D(버리기): D는 첫 번째 수를 버리는 함수 => queue
2) 특정 동작을 의미하는 문자열을 입력 받아 의도한 처리를 하는 프로그램을 만들기
[전략]
1) 무식하게 만들어야지 뭐
"""
for _ in range(int(sys.stdin.readline())):
    method_seq = list(sys.stdin.readline().rstrip())
    N, target_list, checker, count = int(sys.stdin.readline()), deque(eval(sys.stdin.readline().rstrip())), False, 0
    for method in method_seq:
        try:
            if method == 'R':
                count += 1
            else:
                if count % 2 == 1:
                    target_list.pop()
                else:
                    target_list.popleft()
        except:
            print('error')
            checker = True
            break

    if not checker:
        result = '['
        if not list(target_list):
            print('[]')

        elif count % 2 == 0:
            for char in list(target_list):
                result = result + str(char) + ','
            print(result[:-1] + ']')
        else:
            for char in list(reversed(target_list)):
                result = result + str(char) + ','
            print(result[:-1] + ']')

