import sys


def solution():
    """ 소문난 칠공주 영입(이게 도대체 무슨 문제야)
    idea: adj graph search with backtracking
        - 스택 호출: 탐색 가능한 좌표가 있을 때
        - 스택 종료: 현재 길이가 7일 때, 혹은 이미 임도연 파가 4명 이상인 경우
        - 인자 정의: 다음 탐색 위치 좌표
        - 자료 구조: 세트
            - 경우의 수도 될 수 없는 경우의 수도 모두 중복 없이 처리 하려면 세트 써야할 듯
    question:
        - 그래프 탐색 알고리즘이 틀렸음
            - 자료구조를 세트로 잡고, 백트래킹한 것까지 좋았는데, dfs로 가면, 주어진 예제 1번의 2번쨰 정답 케이스를 캐치할 수 없음
            - dfs 대신, bfs를 사용해야 저 케이스를 잡을 수 있을거 같음
            - 아니네, 일반적인 dfs/bfs로 저 케이스 못잡음
            - 개어렵네,,, 뭐지

    reference:
        - https://www.acmicpc.net/board/view/115186

    """
    # backtrack func
    sys.setrecursionlimit(10**6)
    def backtrack(y: int, x: int, vo: int) -> None:
        # end condition 1 of stack
        if vo >= 4:
            return

        # end condition 2 of stack
        if len(path) == 7:
            print(path)
            answer.add(tuple(sorted(list(path))))
            return

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if -1 < ny < 5 and -1 < nx < 5 and not visited[ny][nx]:
                no = vo
                if grid[ny][nx] == "Y":
                    no += 1

                path.add((ny,nx))
                visited[ny][nx] = 1

                backtrack(ny, nx, no)

                path.remove((ny,nx))
                visited[ny][nx] = 0

    input = sys.stdin.readline
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    grid = [list(input().rstrip()) for _ in range(5)]

    # init the data structure for backtracking
    cache = set()
    answer = set()
    visited = [[0]*5 for _ in range(5)]

    # do backtrack
    for i in range(5):
        for j in range(5):
            opp = 0
            if grid[i][j] == "Y":
                opp += 1

            path = set()
            path.add((i,j))
            visited[i][j] = 1

            backtrack(i,j, opp)
            visited[i][j] = 0


    # check the current state of answer
    # print(answer)
    print(len(answer))


def solution2():
    """ 그냥 완전 탐색으로 돌리기만 해도 풀리겠는데, recursive call 필요하네
    idea: backtracking with dfs, combinations
        - 7이란 숫자를 가로, 세로의 크기 쌍으로 표현
            - (7,0), (6,1), (5,2) ... (0,7)
            - 이렇게 쌍으로 표현까지 좋은데, 어떻게 그걸 이어 줄까??
            - 그럼 굳이 dfs, bfs로 그리드 한 칸, 한 칸 탐색할 이유도 없음!

    feedback:
        - recursive call이 필요함
    """
    # init data structure
    grid = [list(input().rstrip()) for _ in range(5)]

    # do backtrack
    answer = set()
    for i in range(5):
        for j in range(5):
            for l in range(2, 5-j):  # range for column axis
                opp = 0
                flag = 0
                path = set()
                path.add((i, j))
                if grid[i][j] == "Y":
                    opp += 1

                for col in range(1, l+1):
                    cnt = grid[i][j+col]
                    if cnt == "Y":
                        opp += 1
                    path.add((i,j+col))
                    if opp >= 4:
                        flag += 1
                        break
                if flag:
                    break

                total = 6-l
                forward_size = total - i
                backward_size = total - forward_size
                for col in range(0, l+1):
                    for fw in range(1, forward_size+1):  # forward range for row axis
                        cnt = grid[i+fw][j+col]
                        if cnt == "Y":
                            opp += 1

                        path.add((i+fw, j+col))
                        if opp >= 4:
                            flag += 1
                            break

                    for bw in range(1, backward_size+1):  # backward range for row axis
                        cnt = grid[i-bw][j+col]
                        if cnt == "Y":
                            opp += 1

                        path.add((i-bw, j+col))
                        if opp >= 4:
                            flag += 1
                            break

                    if not flag:
                        answer.add(tuple(sorted(list(path))))
    print(answer)


def solution4():
    """
    idea: dfs + bfs
        - dfs: 그리드 좌표 25개에서 7개를 중복 없는 조합으로 뽑는 경우의 수 구하기
        - bfs: 구한 좌표 조합의 인접 여부, S가 4개 이상인지 여부
    """
    from collections import deque
    from itertools import combinations

    # init data structure
    input = sys.stdin.readline
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    grid = [list(input().rstrip()) for _ in range(5)]

    # get combinations
    answer = set()
    for comb in combinations(range(25), 7):
        opponent = 0
        team = set()
        cache = set(comb)
        print(cache)
        for c in comb:
            y, x = divmod(c, 5)
            if grid[y][x] == "Y":
                opponent += 1

            if opponent >= 4:
                break

            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if -1 < ny < 5 and -1 < nx < 5 and (ny*5 + nx) in cache:
                    team.add(ny*5 + nx)

        if opponent < 4 and team == cache:
            answer.add(tuple(sorted(list(team))))

    print(answer)
    return


if __name__ == "__main__":
    solution4()
