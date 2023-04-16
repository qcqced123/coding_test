import sys
"""
[풀이 시간]
1) 22:35 ~ 23:05

[요약]
1) N개의 돌
    - 턴마다 1개 혹은 3개씩 가져갈 수 있음
    - 마지막 돌을 가져가는 사람이 승
    - 상근이가 선공, 이기는 사람 구하기
[전략]
1)
"""
N = int(sys.stdin.readline())
if N % 2 == 0:
    print('CY')
else:
    print('SK')
