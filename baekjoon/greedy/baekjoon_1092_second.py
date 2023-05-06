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
N = int(sys.stdin.readline())
c_weight = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
b_weight = list(map(int, sys.stdin.readline().split()))  # Number of Boxes

c_weight.sort(reverse=True), b_weight.sort(reverse=True)
c_check_list, b_check_list, time, checker = [False for _ in range(N)], [False for _ in range(M)], 0, False
queue = deque(b_weight)
while queue:
    for i in range(N):
        if len(queue) == 0:
            break
        box = queue.popleft()
        if box > c_weight[0]:
            print(-1)
            exit()
        if not c_check_list[i] and box <= c_weight[i]:
            c_check_list[i] = True
            continue
        else:
            queue.appendleft(box)
    time += 1
    c_check_list = [False for _ in range(N)]

print(time)
