import sys
from collections import deque
"""
[풀이 시간]
1) 21: 40 ~ 22: 10

[요약]
1) 1분에 박스 하니씩 실을 수 있음
    - 크레인 동시 작동, 무게 제한
    - 최소 시간 구하기
[전략]
1) 박스 중에 크레인 하중보다 무거운거 있으면 무조건 -1 출력
2) 최소 시간 구하기
    - Greedy, 무엇을 어떻게 정렬할 것인가, 어떻게 집합을 나눌 것인가
    - 무거운거 부터 빨리 빨리 붙여주는게 맞지 않나??
    - while loop + queue 사용하면 되겠네
    - 개별 크레인 하중이랑 동일한거 하나 이상인거 있으면 개수
"""
N, c_weight = int(sys.stdin.readline()), list(map(int, sys.stdin.readline().split()))
M, b_weight = int(sys.stdin.readline()), list(map(int, sys.stdin.readline().split()))  # Number of Boxes
c_weight.sort(reverse=True), b_weight.sort(reverse=True)
c_check_list, b_check_list, time, checker = [False for _ in range(N)], [False for _ in range(M)], 0, False

while not checker:

    for i in range(N):
        for j in range(M):
            if not c_check_list[i] and not b_check_list[j] and b_weight[j] <= c_weight[i]:
                c_check_list[i], b_check_list[j] = True, True
                break

    time += 1
    c_check_list = [False for _ in range(N)]
    if False not in b_check_list:
        checker = True

print(time)
