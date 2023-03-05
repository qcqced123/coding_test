import sys
"""
[풀이 시간]
1) 22:30 ~ 23:15

[문제 요약]
1) 길이 L 테이프 무한개: 새는 물 막기
    - 테이프 시작과 끝 지점 결정: 구멍 좌우 0.5만큼 간격을 주기
    - 테이프 자르기 & 겹쳐 이어 붙이기 불가
[전략]
1) 필요한 최소 테이프 개수
    - 시간 압박 크지 않은 문제
    - 구멍 위치를 받는 동시에 루프를 돌리자
2) 구멍 크기를 고려할 필요 없음
    - 구멍 N개가 모두 붙어 있는 경우 => 구멍 개수 == 구멍 길이
    - 정렬이 필요한 자료구조가 지금 있나...?
    - 구멍 개수 / 테이프 길이를 올림 처리하면 => 반례: 구멍의 위치가 서로 멀리 떨어져 있는 경우
    - 구멍 위치 배열을 내림 차순 정렬: 빼서 길이를 구해 줘야 하기 때문에
    - 그냥 구멍 개수랑 길이랑 매칭 시키면 되겠네

"""
# Input
N, L = map(int, sys.stdin.readline().split())
hole_idx, temp, result = list(map(int, sys.stdin.readline().split())), 0, 0
hole_idx.sort(reverse=True) # 내림차순 정렬

for i in range(len(hole_idx)):
    if hole_idx[i] == hole_idx[-1]:
        break
    if temp == L:
        temp = 0
        result += 1
    temp += hole_idx[i] - hole_idx[i+1]
