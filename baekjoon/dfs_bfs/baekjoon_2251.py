import sys
from collections import deque


def solution():
    """
    idea: bfs wtih adj array
        - 개별 물통에 담긴 물의 양을 변수로 표현하기
            - c: 전체 물통의 물의 총량 == 초기 물통 C에 담긴 물의 양
            - x: 물통 A에 담긴 물의 양
            - y: 물통 B에 담긴 물의 양
            - z: 물통 C에 담긴 물의 양
            => z = c - x - y
        - x,y 값의 변화량에 대해서 인접 배열 형식의 그래프 작성
        - 인접 그래프의 원소에 해당 시점 z값을 기록
        - 인접 그래프 원소값은 -1로 초기화

    feedback:
        - 이렇게 직접 그래프를 만들어서 사용해야 하는 문제가 진짜 어려운 듯...!
    """
    # init data structure
    input = sys.stdin.readline
    A, B, C = map(int, input().split())
    visited = [[0]*(B+1) for _ in range(A+1)]

    # do bfs
    answer = []
    q = deque([(0,0)])
    visited[0][0] = 1
    while q:
        vy, vx = q.popleft()  # 현재 A에 남은 물의 양, 현재 B에 남은 물의 양
        z = C - vy - vx
        if not vy:
            answer.append(z)

        # A to B
        water = min(vy, B-vx)  # 한쪽이 텅 비거나, 한쪽이 꽉차는 경우 붓는걸 멈출 수 있기 때문에, 수식이 이런식으로 세워진다
        ny, nx = vy-water, vx+water
        if not visited[ny][nx]:
            q.append((ny, nx))
            visited[ny][nx] = 1

        # A to C
        water = min(vy, C-z)
        ny, nx = vy-water, vx
        if not visited[ny][nx]:
            q.append((ny, nx))
            visited[ny][nx] = 1

        # B to A
        water = min(vx, A-vy)
        ny, nx = vy+water, vx-water
        if not visited[ny][nx]:
            q.append((ny, nx))
            visited[ny][nx] = 1

        # B to C
        water = min(vx, C-z)
        ny, nx = vy, vx-water
        if not visited[ny][nx]:
            q.append((ny, nx))
            visited[ny][nx] = 1

        # C to A
        water = min(z, A-vy)
        ny, nx = vy+water, vx
        if not visited[ny][nx]:
            q.append((ny, nx))
            visited[ny][nx] = 1

        # C to B
        water = min(z, B-vx)
        ny, nx = vy, vx+water
        if not visited[ny][nx]:
            q.append((ny, nx))
            visited[ny][nx] = 1

    answer.sort()
    print(*answer)


if __name__ == "__main__":
    solution()
