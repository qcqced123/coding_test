import sys
"""
[요약]
- 진실을 아는 사람이 한 명이라도 포함된 파티에서는 절대 진실을 말할 수 없다
    - 진실을 아는 사람이 속한 파티에 같이 있는 사람들한테도 모두 진실을 말해야 하는 상황
    - 입력이 크지 않아서 이중 루프를 돌려도 될 것 같음
[풀이]
1) 배열 K의 원소가 들어 있는 모든 파티 리스트 탐색
    - 개별 참여자를 노드로 보고, 진실을 아는 사람이라면 모두 방문 처리
    - 참석자 모두 탐색
        - 진실을 아는 사람이 속한 파티가 가장 마지막에 있는 경우, 어떻게 처리해줄 것인가가 관건인데...
    - 선형 탐색으로 구라칠 수 없는 사람들을 찾아, 리스트 업데이트
    - 업데이트 된 리스트 활용, 전체 파티 다시 순회하면서 구라칠 수 있는 파티 개수 세어주기
"""

N, M = map(int, sys.stdin.readline().split())  # 사람, 파티 숫자
K = set(input().split()[1:])
arr = [set(sys.stdin.readline().split()[1:]) for _ in range(M)]
# 1) 진실을 아는 사람 업데이트
for _ in range(M):
    for party in arr:
        if party & K:
            K = K.union(party)
curr = M
# 2) 업데이트 사람 목록을 이용해 다시 순회
for party in arr:
    if party & K:
        curr -= 1
print(curr)
