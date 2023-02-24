import sys, heapq
"""
Idea: 과제 기한이 많이 남은 쪽부터 거꾸로 접근하자
=> 거꾸로 접근하면 나처럼 복잡하게 케이스를 나눌 필요가 없어진다
=> 항상 명심하자! 구현 문제가 아닌 이상 코딩 테스트에 나오는 문제들은 코드가 단순하다!
"""
# Input & Sort
temp_list, result = [], 0
assign_list = [list(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline()))]
assign_list = sorted(assign_list, key=lambda x: x[0]) # 오름차순 정렬
last_day = assign_list[-1][0]

# 기한이 많이 남은 과제부터 거꾸로 접근
for day in range(last_day, 0, -1):
    while assign_list and assign_list[-1][0] >= day:
        d, w = assign_list.pop()
        heapq.heappush(temp_list, -w) # Heap 활용해 우선순위 큐 구현
    # temp_list에 원소가 있을 때, 마감 기한이 현재 날짜인 과제 모두 순회한 경우
    if temp_list:
        result += -(heapq.heappop(temp_list))

print(result)





