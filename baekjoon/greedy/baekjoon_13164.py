import sys
"""
[풀이 시간]
1) 18:35 ~ 19:15

[요약]
1) N명을 키 순서, K개의 하위 그룹 분할
    - 그룹에 적어도 한 명 이상 존재, 그룹별 인원수 상이
    - 같은 그룹은 인접: 키가 비슷한 사람, 같은 그룹에 속함
2) 티셔츠 비용 최소화
    => 비용: 조에서 가장 큰 사람 - 가장 작은 사람
[전략]
1) 시간 압박이 있는 문제
    - 힙정렬 고려
2) 비용의 최소화
    - Greedy, 어떤 대상 & 어떻게 정렬할 것인가
    - 결국 아까 풀었던 1080번과 유사한 문제
"""
N, K = map(int, sys.stdin.readline().split())
child_list, cost_list = list(map(int, sys.stdin.readline().split())), []
for i in range(N-1):
    cost_list.append(child_list[i+1] - child_list[i])
cost_list.sort(reverse=True)
print(sum(cost_list[K-1:]))


