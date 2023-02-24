import sys, heapq

"""
[풀이 시간]
1) 15:50 ~ 16:40

[문제]
1) 두 묶음을 하나의 묶음으로 합칠 때 => (개수 + 개수) = 비교 수
2) 주어진 모든 카드 묶음에서 2개씩 짝지어 합쳐, 최종적으로 한 개의 묶음을 만들 때 최소 비교 숫자를 구하세요 

[변수]
N => 주어진 카드 묶음의 수
A => 첫 번째 묶음 카드 수
B => 두 번째 묶음 카드 수

[아이디어]
1) 일단 중간 저장해주는게 필요할테고, 다익스트라랑 비슷한거 같은데
=> 그룹 지어주는거랑 같은거 같은데
10, 20, 40, 50이 있다고 가정 => 가장 작은거 계속 고르는게 좋은 것 같은데..?
(10 + 20) + (30 + 40) + (70 + 50) = 30 + 70 + 120 = 220
(10 + 50) + (60 + 20) + (80 + 40) = 60 + 80 + 120 = 260
2) 정렬이 되어 있다니까 그냥 순서 대로 빼서 더해주면 되는거 아닌가
3) heap 정렬을 사용하자
"""
# Input
N = int(input())
num_list = [int(input()) for i in range(N)]
result_list = []
checker = True
temp = 0


def min_heapsort(iterable):
    h = []
    result = []
    # heap에 원소 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # heap으로부터 원소 빼내기
    for _ in range(len(h)):
        result.append(heapq.heappop(h))

    return result

# 리스트 내부 남은 원소들과 비교
while checker:
    if len(num_list) == 1:
        break
    num_list = min_heapsort(num_list) # 여기 정렬이 문제구나....
    temp = num_list[0] + num_list[1]
    for _ in range(2):
        num_list.remove(num_list[0])

    num_list.append(temp)
    result_list.append(temp)

print(sum(result_list))

