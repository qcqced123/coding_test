import sys, heapq
"""
[풀이 시간]
1) 00:00 ~ 00:45

[문제 요약]
1) 기타 줄 N개가 끊어진 상황 => 최소 비용으로 교체
  - 6줄 패키지 혹은 낱개로 여러개 구매 가능
  - 브랜드 M개 => (6줄 짜리 가격, 낱개 가격)
[전략]
1) 최소 비용: Greedy
2) 입력을 정렬: 앞뒤 두가지 기준 정렬 배열 구현
    - 꼭 같은 브랜드끼리 묶어서 정렬할 필요가 없음
    - N 크기에 따라서 케이스 분류
"""
N, M = map(int, sys.stdin.readline().split())
six_line, one_line, result = [], [], 0

for _ in range(M):
    six_cost, one_cost = map(int, sys.stdin.readline().split())
    heapq.heappush(six_line, six_cost) # six_line
    heapq.heappush(one_line, one_cost) # one_line

if N <= 6:
    result = min(heapq.heappop(six_line), heapq.heappop(one_line) * N)
else:
    counter, one_cost, six_cost = int(N / 6), heapq.heappop(one_line), heapq.heappop(six_line)
    temp1 = N * one_cost
    temp2 = (counter * six_cost) + (N - counter*6) * one_cost
    if isinstance(N/6, float):
        temp3 = (counter + 1) * six_cost
    else:
        temp3 = counter * six_cost
    result = min(temp1, temp2, temp3)
print(result)




