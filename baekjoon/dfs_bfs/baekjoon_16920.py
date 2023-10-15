import sys
from collections import deque


def solution():
    N, M, P = map(int, sys.stdin.readline().split())
    scores = [0] * (P + 1)

    dy = [0, 0, 1, -1]  # direction of search
    dx = [1, -1, 0, 0]

    p_list = [0] + list(map(int, sys.stdin.readline().split()))  # for matching index with player num
    graph = [[0]*M for _ in range(N)]
    player_q = [deque() for _ in range(P+1)]  # for matching index with player num

    # 1) player dict 초기화
    for i in range(N):
        tmp = sys.stdin.readline().rstrip()
        for j in range(M):
            if tmp[j] == ".":
                continue
            elif tmp[j] == "#":
                graph[i][j] = -1
            else:
                now = int(tmp[j])
                graph[i][j] = now
                player_q[now].append([i, j])
                scores[now] += 1

    # 2) 개별 player 탐색
    turn = True
    while turn:
        turn = False
        for player in range(1, P+1):
            if not player_q[player]:  # 이미 탐색이 종료된 플레이어 턴 스킵
                continue
            q = player_q[player]
            for _ in range(p_list[player]):
                if not q:  # 모든 플레이어들이 1개 이상 영역 확장 못하는데 최대 탐색 깊이가 매우 큰 경우, 헛돌게 된다
                    break
                for _ in range(len(q)):
                    vy, vx = q.popleft()
                    for i in range(4):
                        ny = dy[i] + vy
                        nx = dx[i] + vx
                        if -1 < ny < N and -1 < nx < M and graph[ny][nx] == 0:
                            graph[ny][nx] = player
                            scores[player] += 1
                            q.append([ny, nx])
                            turn = True
    print(*scores[1:])


if __name__ == "__main__":
    solution()
