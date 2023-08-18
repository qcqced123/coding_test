import sys
"""
[풀이 시간]
1) 21:35 ~ 22:05

[요약]
1) 병든 나이트가 N × M 크기 체스판의 가장 왼쪽 아래 칸에 위치
    - 2칸 위로, 1칸 오른쪽 => 3칸
    - 1칸 위로, 2칸 오른쪽 => 3칸
    - 1칸 아래로, 2칸 오른쪽 => 3칸
    - 2칸 아래로, 1칸 오른쪽 => 3칸
    => 이동 방식이 겹치는 영역이 꽤 많다
2) 이동 횟수가 4번
    - 보다 많다면, 이동 방법을 모두 한번씩
    - 보다 적다면, 제약이 없음
[전략]
1) 최대 칸수 & 이동 방식 옵션 4개: Greedy
    - 세로의 길이만 고려해 경우의 수를 줄이자
"""
N, M = map(int, sys.stdin.readline().split())

if N == 1:
    print(1)
elif N == 2:
    print(min(4, (M + 1) // 2))  # 최대 이동 횟수가 3이라서, 이 때 최대 방문 칸은 4칸
elif M < 7:
    print(min(4, M))
else:
    print(M-2)
