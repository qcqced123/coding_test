import sys
"""
[풀이 시간]
1) 12:40 ~ 01:20

[규칙]
1) 양팔 저울: 한 쪽에는 물건, 다른 한 쪽에는 무게추
2) 측정 불가능 양의 정수 무게 중 최소값 구하기

[변수]
N => 양의 정수 무게를 가진 무게추 개수

[전략]
1) N이 최대 1000개라서 시간 초과 압박은 크게 없다 (이중 루프까지도 가능함)
2) 추를 올려 놓는 모든 경우의 수에서 최대, 최소를 구해서 빼면 범위가 나올 것
=> 범위 최소부터 시작해서 +1씩 늘려가다가 모든 경우의 수 리스트에 없는 애가 정답 아닐까?
=> 최대 최소 구해서 리스트 쫙 펼쳐두고 pop으로 빼고 min(list()) 하면 되지 않을까
=> 일단 최소 힙정렬을 사용해보자
"""
# Input & Min Sort
target, N = 1, int(sys.stdin.readline())
weight_list = sorted(list(map(int, sys.stdin.readline().split())))
for weight in weight_list:
    if target < weight:
        break
    target += weight
print(target)


