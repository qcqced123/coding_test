from collections import deque, defaultdict


def my_solution(n, wires):
    """
    1) wires 선형 순회
      - 하나씩 빼보면서 최소값 계산하기
      - 인덱스 기반으로 순회
      - wires 길이와 전체 노드 개수는 다르다는 점을 명심하자

    2) 노드 개수 세기: DFS or BFS
      - 좀 더 디버깅 하기 쉬운 BFS 선택
    => 제발 코드 쓰기 전에, 구현 필요한 세부사항들 주석에 적고, 구현했는지 안했는지 체크하기
    => 그래야 실수를 안함
    """

    def bfs(x: int) -> int:
        total = 1
        visit.append(x)
        q = deque([x])
        while q:
            vx = q.popleft()
            for next_x in graph[vx]:
                if next_x != -1 and next_x not in visit:
                    total += 1
                    visit.append(next_x), q.append(next_x)
        return total

    answer = 9999999999
    visit, result = [], []
    graph = defaultdict(list)  # 나중에 clear() 사용해서 재활용
    for i in range(len(wires)):
        curr_wire = wires[:i] + wires[i + 1:]
        for v1, v2 in curr_wire:
            graph[v1].append(v2), graph[v2].append(v1)

        for node in range(1, n + 1):  # remove, 애
            if node in graph:
                continue
            graph[node].append(-1)

        for node in range(1, n + 1):
            if node not in visit:
                visit.append(node)
                result.append(bfs(node))

        answer = min(answer, abs(result[0] - result[1]))
        graph.clear(), visit.clear(), result.clear()
    return answer


def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    for a,b in wires:
        graph[a].append(b), graph[b].append(a)

    def dfs(node, parent):
        cnt = 1
        for child in graph[node]:
            if child != parent:
                cnt += dfs(child, node)
        return cnt

    min_diff = float('inf')
    for a,b in wires:
        graph[a].remove(b)
        graph[b].remove(a)

        cnt_a = dfs(a, b)
        cnt_b = n - cnt_a

        min_diff = min(min_diff, abs(cnt_a - cnt_b))
        graph[a].append(b)
        graph[b].append(a)
    return min_diff