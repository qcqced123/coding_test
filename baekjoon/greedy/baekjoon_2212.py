import sys
"""
[풀이 시간]
1) 14:50 ~ 15:30

[요약]
1) N개의 센서, K개의 집중국
    - 센서는 적어도 하나의 집중국과 통신, 집중국 수신 가능 영역 길이 합 최소
    - 도로는 평면 위 직선, 정수 거리로 표현
    - 집중국의 수신 가능영역 길이는 0이상

[전략]
1) 시간 제한 넉넉함: 이중 루프까지는 괜찮을 것 같음
2) 수신 가능 길이 합의 최솟값
    - Greedy, 무엇을 어떻게 정렬할 것인지 고민
    - 주어진 센서 리스트를 K개의 하위 그룹으로 나누는 것이 목표
    - 집중국은 센서들이 많이 모여 있는 곳 사이에 두는 것이 가장 좋기 때문
    - 센서들 사이의 거리를 구해서 리스트에 담고 내림 차순으로 정렬
    - 내림 차순 기준 K-1개의 거리를 제외한 나머지 거리의 합이 수신 가능 길이의 최소값
"""
N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
sensor_list, dist_list = list(map(int, sys.stdin.readline().split())), []
sensor_list.sort()

for i in range(N-1):
    dist_list.append(sensor_list[i+1] - sensor_list[i])
dist_list.sort(reverse=True)
print(sum(dist_list[K-1:]))

