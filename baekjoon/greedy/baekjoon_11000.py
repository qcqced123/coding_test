import sys, heapq
"""
[풀이 시간]
1) 20:40 ~ 21:40

[문제 요약]
1) S시에 시작해서 T시에 끝나는 N개의 수업
    - 강의실을 최소로 사용하면서 N개의 모든 수업을 해야 하는 상황
    - 모든 수업은 수업이 끝난 직후부터 강의가 가능
[전략]
1) 시간 압박이 상당한 문제
    - 시간 최대한 줄여야 할 듯
2) 강의실을 최소한으로 사용: Greedy
    - 힙 정렬이 제대로 되지 않기 때문에 일단 리스트에 다 저장하고 sorted & lambda 사용 하는게 나을 것 같음
    - 는 개뿔... 시간 초과해서 결국 힙 정렬 사용
3) 무엇을 기준으로 정렬할 것인가
    - 시작 시간 기준 오름 차순 정렬
    - 다 돌지도 않고 추가해버리니까 그렇지....
"""
N = int(sys.stdin.readline())
lecture_list, classroom, result, min_value = [], [], 0, 0

for _ in range(N):
    lecture_list.append(list(map(int, sys.stdin.readline().split())))

lecture_list = sorted(lecture_list, key=lambda x: x[0])
for i in range(len(lecture_list)):
    if i == 0:
        heapq.heappush(classroom, lecture_list[i][1])
        result += 1
        continue

    if classroom[0] <= lecture_list[i][0]:
        heapq.heappop(classroom)
        heapq.heappush(classroom, lecture_list[i][1])
        continue
    else:
        result += 1
        heapq.heappush(classroom, lecture_list[i][1])
print(result)

