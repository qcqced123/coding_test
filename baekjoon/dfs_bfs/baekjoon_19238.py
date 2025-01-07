import sys
from collections import deque


def solution():
    """ 도착지 == 연료 충전소, not 연료 == 영업 종료
    idea: graph simulation with bfs
        - 승객 선택 기준: 현위치에서 최단 거리, 행번호, 열번호
        - 도착 성공: 사용한 연료의 두 배
        - 리턴: 성공하고 남은 연료의 양

    feedback:
        - 현재 택시 위치 == 승객 위치
        - 현재 택시 위치 to 승객 위치 못 가는 케이스 (벽 때문에)
        - 현재 승객 위치 to 목적지 못 가는 케이스 (벽 때문에)

    reference:
        - https://www.acmicpc.net/board/view/58022
    """
    # func for updating the shortest path
    def find_customer(y: int, x: int):
        cost = INF
        target = []
        q = deque([(0, y, x)])
        visited = set()
        visited.add((y,x))
        while q:
            vc, vy, vx = q.popleft()
            for i in range(4):
                nc, ny, nx = vc+1, vy + dy[i], vx + dx[i]
                if nc <= cost and -1 < ny < N and -1 < nx < N and not grid[ny][nx] and (ny, nx) not in visited:
                    if (ny, nx) in customers:
                        if nc == cost:
                            target.append((ny, nx))
                        else:
                            cost = nc
                            target = [(ny, nx)]
                    else:
                        q.append((nc, ny, nx))
                        visited.add((ny, nx))

        target.sort()
        return (cost, target[0][0], target[0][1]) if target else None

    def calculate_energy(y: int, x: int):
        visited = set()
        visited.add((y, x))
        q = deque([(0, y, x)])
        while q:
            vc, vy, vx = q.popleft()
            for i in range(4):
                nc, ny, nx = vc+1, vy + dy[i], vx + dx[i]
                if ny == ty and nx == tx:
                    return nc

                if -1 < ny < N and -1 < nx < N and not grid[ny][nx] and (ny, nx) not in visited:
                    q.append((nc, ny, nx))
                    visited.add((ny, nx))

    # get input data
    INF = sys.maxsize
    input = sys.stdin.readline
    N, M, E = map(int, input().split())
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    grid = [list(map(int, input().split())) for _ in range(N)]
    sy, sx = map(int, input().split())
    sy -= 1
    sx -= 1

    # init the data structure
    customers = set()
    destinations = dict()
    for _ in range(M):
        fy, fx, ey, ex = map(int, input().split())
        fy -= 1
        fx -= 1
        ey -= 1
        ex -= 1
        customers.add((fy, fx))
        destinations[(fy, fx)] = (ey, ex)

    # do simulation with bfs
    while customers:
        # 현재 택시 위치 == 승객 위치도 예외 처리
        cc, cy, cx = 0, sy, sx

        # 현재 택시 위치에서 출발지 자체로 못가는 경우 예외 처리
        if (sy, sx) not in customers:
            checker = find_customer(sy, sx)
            if checker is not None:
                cc, cy, cx = checker
            else:
                print(-1)
                return

        ty, tx = destinations[(cy, cx)]
        # remove current customer's data at cache
        customers.remove((cy, cx))
        destinations.pop((cy, cx))

        # calculate the lower bound of energy for reaching the destination
        E -= cc
        if E <= 0:
            print(-1)
            return

        cost = calculate_energy(cy, cx)
        if cost is None:  # 출발지에서 도착지로 못가는 경우 처리
            print(-1)
            return

        # check if current path is movable
        # True: update the starting point position
        # False: end the stack
        E -= cost
        if E >= 0:
            E += 2*cost
            sy, sx = ty, tx  # if success

        else:
            print(-1)
            return

    print(E)


if __name__ == "__main__":
    solution()
