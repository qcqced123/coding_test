import sys
"""
[풀이 시간]
16:35 ~ 17: 15

[문제 요약]
1) R*C 격자로 빵집 위치 표현, 첫번째 열은 다른 빵집 가스관, 마지막 열은 원웅이 가스관
2) 중간에 건물이 있는 경우, 가스관 설치 불가 격자 위에 X로 건물 표현
3) 가스관 이동 가능 방향은 3가지, 가스 파이프라인 최대 개수

[전략]
- 시간 압박은 크지 않은 문제
- 가스 파이프라인 설치한 곳은 정수 1로 표현하자
- 3가지 방향 이동을 인덱스로 표현해주는데, 3가지 방향 모두 이동 불가할 때 해당 탐색은 종료시키기
  1열의 원소별로 루프를 돌려주자
  가스 파이프라인 개수가 최대가 되게 만드려면, 이동 방향에 대한 우선순위를 정해주자!
  nx가 C-1에 도달하면 더이상 파이프라인 세지 말고 끝내야지
"""


def move(gas_map, y, x):
    if gas_map[y][x] == '.':
        gas_map[y][x] = 1
    else:
        return
    for i in range(3):
        nx = x + 1
        ny = y + dy[i]
        if nx >= C or ny < 0 or ny >= R:
            continue
        move(gas_map, ny, nx)
        if nx == C-1:
            break

R, C = map(int, sys.stdin.readline().split())
gas_map, visited, result, = [list(sys.stdin.readline().rstrip()) for _ in range(R)], [], 0
# direction
dy = [-1, 0, 1] # 이동 방향의 우선순위: 항상 우측 대각선 상단부터

for i in range(R):
    move(gas_map, i, 0)

for i in range(R):
    if gas_map[i][C-1] == 1:
        result += 1
print(result)
