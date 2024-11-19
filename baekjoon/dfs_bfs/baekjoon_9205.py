import sys
from collections import deque


def solution():
    """ 맥주 20개, 50미터당 한 병(하마..?), 제약 조건: 맥주 20병 이하
    제약 조건을 만족하는 경로 유무 찾기, 인접 행렬
    input:
        - 인접 행렬 자체를 안주고 내가 만들어야 되네

    idea: bfs or dfs
        - 1차원 배열 bfs
        - 남은 맥주로 갈 수 있는 모든 곳 탐색하고, 갈 수 있는 곳 큐에 넣기
            - 뒤로갈 이유가 없음, 어차피 중간 경유지가 편의점이라서
        - 다음 경유지 갈 수 있는지 여부 체크하기
            - 갈 수 있다면, 경유지 성격에 따라서 분기
            - 없다면, 종료
    question:
        - 왜 맞는거지...?
        - 현 위치에서 남은 맥주로 갈 수 있는곳을 탐색하는데 왜 뒤쪽도 탐색하게 만드는데 맞는거지..?
        - 앞쪽만 봐도 맞아야 되는거 아닌가...? 다음거 풀고 생각해보자

    """
    input = sys.stdin.readline
    for _ in range(int(input())):
        # init the data structure
        n = int(input())  # number of convenience stores
        grid = [tuple(map(int, input().split())) for _ in range(n+2)]  # house - store - convert
        visited = [0]*(n+2)

        # do the bfs for finding the PATH to convert hall
        remain = 20  # current state of rest beer
        cnt_y, cnt_x = grid[0][0], grid[0][1]
        end_y, end_x = grid[-1][0], grid[-1][1]

        flag = False
        visited[0] = 1
        q = deque([(0, cnt_y, cnt_x, remain)])
        while q:
            vi, vy, vx, vb = q.popleft()  # 방문 배열 인덱스, 좌표, 남은 맥주
            for i in range(n+2):
                if visited[i]:
                    continue

                next_y, next_x = grid[i][0], grid[i][1]
                minimum, remain = divmod(abs(next_y - vy) + abs(next_x - vx), 50)
                if remain: minimum += 1
                if minimum <= vb:
                    if next_y == end_y and next_x == end_x:
                        flag = True
                        print("happy")
                        break

                    visited[i] = 1
                    q.append((i, next_y, next_x, 20))

            if flag:
                break

        else:
            print("sad")


if __name__ == "__main__":
    solution()
