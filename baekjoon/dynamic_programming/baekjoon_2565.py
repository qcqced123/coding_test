import sys
from typing import List
"""
[요약]
1) 두 전봇대 A와 B 사이에 하나 둘씩 전깃줄을 추가하다 보니 전깃줄이 서로 교차하는 상황
    - 몇 개를 없애서 교차하지 않도록 최소한의 전깃줄 없애기
    - 시간 제한: 1초
    - 메모리: 넉넉함
    - 입력:
[전략]
1) Greedy or DP
    - 방향성이 다른 전깃줄을 없애면 된다.
    - A>B: 전깃줄이 아래
    - A<B: 전깃줄이 위로
    => 뭘 어떻게 접근해야 하는거지..?
"""
N = int(sys.stdin.readline())
lines = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


