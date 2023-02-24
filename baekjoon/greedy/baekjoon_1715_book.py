import heapq, sys

"""
[Re-Try]
1) 숫자 묶음을 입력 받으면서 힙 정렬을 수행 시키자
"""

# Input
num_list = []
result = 0

# Heap push => 이런 방식으로도 한 줄씩 들어오는 입력을 받을 수 있구나
for i in range(int(sys.stdin.readline())): # Input N
    heapq.heappush(num_list, int(sys.stdin.readline())) # Input Num_list

# 예외 처리 => 1개 받는 경우
if len(num_list) == 1:
    print(0) # 아 1개 받는 경우에는 합칠 필요가 없기 때문에 그렇구나!

else:
    while len(num_list) > 1:
        temp = heapq.heappop(num_list) + heapq.heappop(num_list) # 오름차순으로 Pop
        result += temp
        heapq.heappush(num_list, temp)

    print(result)


