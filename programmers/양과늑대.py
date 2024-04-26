from collections import defaultdict, deque


def solution(info, edges):
    """
    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/92343

    summary:
        1) 이진트리 그래프: 노드 종류는 늑대 or 양
          - 양 <= 늑대: 모든 양 사라짐
        => 양 안사라지게 하면서, 최대한 많은 양 수집해 루트로 복귀
    """

    def build_tree():
        tree = defaultdict(list)
        for edge in edges:
            src, end = edge
            tree[src].append(end)
        return tree

    answer = 0
    tree = build_tree()
    queue = deque([(0, 1, 0, set())])  # current node, nums of sheep, nums of wolfs, visit array
    while queue:
        vy, vs, vw, visited = queue.popleft()
        answer = max(answer, vs)
        visited.update(tree[vy])  # add neighbor node into visit array, update() == add()
        for ny in visited:
            if info[ny]:
                if vs != vw + 1:
                    queue.append((ny, vs, vw + 1, visited - {ny}))
            else:
                queue.append((ny, vs + 1, vw, visited - {ny}))

    return answer


def review_solution(info, edges):
    """
    1) 평범한 BFS 탐색
    2) 큐에 들어 가는 정보를 늘리기
      - BFS로 탐색하되, DFS처럼 해당 탐색 당시의 모든 상태를 저장하는 효과가 생김
      - BFS + DFS라고 보면 될 듯
    """
    def build_tree():
        tree = defaultdict(list)
        for edge in edges:
            src, end = edge
            tree[src].append(end)
        return tree

    answer = 0
    tree = build_tree()

    def bfs(src: int):
        q = deque([(src, 1, 0, set())])  # 시작 노드, 양 몇마리, 늑대 몇마리, visit 배열
        while q:
            vx, vs, vw, visited = q.popleft()
            answer = max(answer, vs)
            visited.add(tree[vx])
            for nx in visited:
                if info[nx]:
                    if vs != vw + 1:
                        q.append((nx, vs, vw+1, visited-{nx}))
                else:
                    q.append((nx, vs+1, vw, visited-{nx}))
    bfs(0)

    return answer
