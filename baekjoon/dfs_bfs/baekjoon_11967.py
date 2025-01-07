import sys
from collections import deque, defaultdict


def solution2():
    """
    idea: bfs
        - 정답 카운트는 현재 방문한 방에서 킬 수 있는 스위치 개수
        - 이동은 인접한 곳만 가능하고 그 중에서 불이 켜져 있는 경우만 실제 방문이 가능
        - 행동을 잘 쪼개서 생각해보자
        - 일단 방문을 해
        - 그다음, 스위치를 켜서, 다른 방의 불을 죄다 켜
            - "불을 키다" == 그리드 값을 바꾸다
            - 불 키는 것도 미리 키면 안되고, 완전히 방문하고 나서, 켜야함
            - 이게 이동하는 시점이랑 불켜지는 시점이 달라서, 움직일 당시에는 불이 안켜져서 넘어갔던게, 나중에는 불이 켜져서 도달할 수도...
            => 이런 케이스 처리하기 위해서, 새롭게 업데이트 되기 전까지 계속 그리드 업데이트 수행, 마지막에 한 번 값 계산
            => 근데 루프 종료 컨디션을 어떻게 잡아야 깔끔하려나??

    feedback:
        - pypy3으로 통과, 이미 방문 했던 곳을 중복으로 방문해야 새롭게 생긴 위치도 다시 방문이 가능한데, 이거 어떻게 최적화 할까

    reference:
        - https://www.acmicpc.net/board/view/54505
    """
    # bfs func
    def bfs(y: int, x: int):
        answer = 0
        visited = set()
        visited.add((0,0))
        q = deque([(y, x)])
        while q:
            vy, vx = q.popleft()
            # turn on the switch
            for sy, sx in switches[(vy,vx)]:
                if not grid[sy][sx]:
                    grid[sy][sx] = 1
                    answer += 1

            for i in range(4):
                ny, nx = vy + dy[i], vx + dx[i]
                if -1 < ny < N and -1 < nx < N and grid[ny][nx] == 1 and (ny,nx) not in visited:
                    q.append((ny,nx))
                    visited.add((ny,nx))

        return answer

    # get input data
    input = sys.stdin.readline
    N, M = map(int, input().split())
    grid = [[0] * N for _ in range(N)]
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)

    # get connection information
    switches = defaultdict(set)
    for _ in range(M):
        py, px, cy, cx = map(int, input().split())
        switches[(py-1,px-1)].add((cy-1, cx-1))

    answer = 1
    grid[0][0] = 1
    while True:
        cnt = bfs(0,0)
        answer += cnt
        if not cnt:
            break

    print(answer)


if __name__ == "__main__":
    solution2()
