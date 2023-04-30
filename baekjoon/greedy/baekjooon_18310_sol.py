import sys
"""
[풀이 시간]
1) 19:00 ~ 19:20

[요약]
1) 일직선 도로 위 마을에 안테나 설치
    - 안테나로부터 모든 집의 거리가 최소가 되도록 위치 설정
    - 하위 그룹화 문제
[전략]
1) 거리 최소: Greedy, 무엇을 어떻게 정렬할 것인가 고민
    - 집 위치를 먼저 정렬하자
"""
N = int(sys.stdin.readline())
house_idx = list(map(int, sys.stdin.readline().split()))
house_idx.sort()
print(house_idx[(N-1) // 2])
