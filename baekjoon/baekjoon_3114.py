import sys
from collections import deque


def solution():
    """ 나무 == 국경선, 3각 방향 탐색,
    idea: bfs with adj array
        - visited: 일방 통행만 허용해서, 굳이 방문 경로를 저장할 이유가 없음
        - queue: y, x, apple, banana
        - 미리 전체 전역 정보를 알고 있어야 시간 제한 맞출 수 있지 않을까??
        - 전체 전역 정보를 미리 캐싱 해두고, 경로를 선택할 때마다 상수 시간에 업데이트 가능하도록

    question:
        - 미리 그리드 전역 정보를 캐싱 해줄 방법을 모르겠음!
    """
    # bfs func
    def bfs():
        q = deque([])
        visited = set()
        while q:
            pass

        return

    # get input data
    input = sys.stdin.readline
    dy, dx = (0, 1, 1), (1, 0, 1)
    R, C = map(int, input().split())
    grid = [list(map(str, input().split())) for _ in range(R)]

    # do bfs
    bfs()


if __name__ == "__main__":
    solution()
