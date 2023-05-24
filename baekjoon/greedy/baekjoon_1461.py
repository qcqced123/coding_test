import sys
"""
[풀이 시간]
1) 12:40 ~ 13:10

[요약]
1) 세준이는 현재 0에 있고, 사람들이 마구 놓은 책도 전부 0에 위치
    - 모든 책을 원위치 시킬 때, 필요한 최소 걸음 수
    - N: 책 개수
    - M: 세준이가 한 번에 들 수 있는 책 개수
    - 책의 위치는 절대 0이 아님, 한 걸음에 한 칸
[전략]
1) 옵션이 여러 개, 최소값 구하기: Greedy
    - 정렬, 경우의 수 최소화 방법 생각
    - N, M 크기에 따라서 케이스 분류
        1-1) M >= N
            부호에 따라서 케이스 분류: 둘 다 같으면 절대값 큰거, 다르면 복잡,,,
        1-2) N > M
            원점에서 거리 가까운 것(절댓값 작은 거)부터 처리
"""
N, M = map(int, sys.stdin.readline().split())
position_list = list(map(int, sys.stdin.readline().split()))

if M >= N:
    position_list.sort(reverse=True)

else:



