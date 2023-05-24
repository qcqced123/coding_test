import sys
"""
[풀이 시간]
1) 22:30 ~ 22:45

[요약]
1) 로프 N개
    - 들 수 있는 중량이 모두 다름
    - 여러 개의 로프를 병렬로 연결 하면 각각의 로프에 걸리는 중량을 나눌 수 있다.
    - k개의 로프, 중량 w인 물체 => 각 로프에 w/k의 중량이 걸리게 된다.
    - 모든 로프를 사용해야 할 필요는 없으며, 임의로 몇 개의 로프를 골라서 사용 가능
[전략]
1) 최대 중량을 구하는 것이 목표
    - Greedy
    - 무엇을 어떻게 정렬, 경우의 수를 최대한 줄이는 방향(forward/backward)
    - 예제를 보니까 단일 물체의 중량을 구해야 하는 것 같음
    - 내림 차순 정렬 & Max(이전까지 최대값, 현재 시점 로프 용량 * 가능한 로프 수)
    - 할당하는 형태는 sorted, 그냥 선언만 하는 형태는 sort
"""
N, result = int(sys.stdin.readline()), 0
loaf_list = sorted([int(sys.stdin.readline()) for _ in range(N)], reverse=True)
for i in range(N):
    result = max(result, loaf_list[i] * (i+1))
print(result)
