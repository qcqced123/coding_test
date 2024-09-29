import sys
from collections import deque
from collections import defaultdict


def solution():
    """ 스타크래프트 건물 짓기, 건물 선행 순서 매번 변경, 건설 시간 존재, N^2logN
    특정 건물을 가장 빨리 짓는 최소 시간

    idea: bfs with dynamic programming
        1) 그래프 구조 생성
        2) 루트 노드 찾기
        3) 캐시 배열 생성
        4) 큐 생성

    => 위상정렬 모른채로 잘 풀었는데, 단점은 예제1번의 마지막 케이스처럼, 하나의 노드에 연결된 incoming 엣지가 여러 개, 불필요하게 큐에 여러번
    삽입되고, 그만큼 불필요한 연산이 많아진다는 것
    => 위상정렬 배열만 추가로 도입해서 그부분만 막아도 알고리즘을 크게 변경하지 않아도 될 것 같다.

    """
    for _ in range(int(input())):
        N, K = map(int, sys.stdin.readline().split())
        time = [0] + list(map(int, sys.stdin.readline().split()))

        # initialize the graph structure
        graph = defaultdict(list)
        nodes = [0]*N
        for _ in range(K):
            src, end = map(int, sys.stdin.readline().split())
            graph[src].append(end)
            nodes[end-1] += 1  # 이 부분을 덧셈으로 변경만 해도 위상 정렬의 배열이 되는군

        # get number of root node
        # initialize the queue for bfs
        # initialize the cache array (dynamic programming)ㄴ
        result = 0
        q = deque([])
        cache = [0] * (N + 1)
        for i in range(N):
            if not nodes[i]:
                q.append(i+1)
                cache[i+1] = time[i+1]

        # get target node
        target = int(input())
        while q:
            vx = q.popleft()
            for nx in graph[vx]:
                # add topological sorting
                nodes[nx-1] -= 1
                if not nodes[nx-1]:
                    q.append(nx)

                cache[nx] = max(cache[nx], cache[vx]+time[nx])

        result = max(result, cache[target])
        print(result)


if __name__ == "__main__":
    solution()
