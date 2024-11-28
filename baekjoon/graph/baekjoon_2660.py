import sys


def solution():
    """
    idea: floyd-warshall
        - 모든 노드 to 모든 노드 최단 경로 찾기
    """
    # init data structure
    INF = sys.maxsize
    input = sys.stdin.readline
    N = int(input())
    grid = [[INF]*(N+1) for _ in range(N+1)]
    while True:
        src, end = map(int, input().split())

        # end point of loop
        if src == -1 and end == -1:
            break

        grid[src][end] = 1
        grid[end][src] = 1

    # do floyd-warshall
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if i != j:
                    grid[i][j] = min(grid[i][j], grid[i][k] + grid[k][j])

    # answering the question
    cache = INF
    answer1, answer2 = [], []
    for i in range(1, N+1):
        player = i
        curr = -INF
        for j in range(1, N+1):
            cnt = grid[i][j]
            if cnt == INF:
                continue

            if cnt > curr:
                curr = cnt

        if curr < cache:
            answer2 = [player]
            cache = curr

        elif curr == cache:
            answer2.append(player)

    print(cache, len(answer2))
    print(*answer2)


if __name__ == "__main__":
    solution()
