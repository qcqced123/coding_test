import sys
from collections import deque, defaultdict


def solution():
    """ 자신의 순서를 알 수 있는 노드 개수
    아까 손으로 풀 때, 하던게 N-1게와 연결된 노드 찾기였는데 그게 맞았음
    아까 그거 하다가 말았던 이유는 그걸 어떻게 구현해야할지 몰라서
    근데 생각해보면, 플루이드 워셜은 경유지 통한 경로를 다 방문하면서 체크하기 때문에, 자신과 연결된 노드가 몇갠지 정확히 세어줄 수 있네
    연결이 되는건지만 기록하면 되서, 굳이 무한대로 값 초기화할 필요 없다

    idea: floyd-warshall
        - N-1 == income + outcome
    """
    # init the data structure
    input = sys.stdin.readline
    N, M = map(int, input().split())
    cache = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        src, end = map(int, input().split())
        cache[src][end] = 1

    # do the dynamic programming for floyd-warshall
    for k in range(1, N+1):
        for y in range(1, N+1):
            for x in range(1, N+1):
                if cache[y][k] and cache[k][x]:
                    cache[y][x] = 1

    # count the number of income and outcome node
    answer = 0
    for i in range(1, N+1):
        cnt = 0
        for j in range(1, N+1):
            cnt += cache[i][j] + cache[j][i]
        if cnt == N-1: answer += 1

    print(answer)


if __name__ == "__main__":
    solution()
