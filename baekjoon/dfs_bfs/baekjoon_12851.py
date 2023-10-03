import sys
from typing import Tuple
from collections import deque
"""
[요약]
1) 숨바꼭질 문제
    - 조건은 모두 동일
[풀이]
1) 가장 빨리 도착하는게 최단 시간이라고 가정
    - 그럼 최단 시간값은 업데이트 될 일이 없고, 같은 값인 애들만 세어주면 되겠네
    - 조건문만 추가할 경우(시간값만 가지고 비교하는 경우) 문제가 발생
        - 1to3은 1->1+1->2+1, 1->1*2-> 2+1 이렇게 두개의 최적 경로가 나오는데 하나만 남게 된다.
        => 그래서 개수를 저장하는 아이가 따로 있어야 함
"""


def bfs(x: int, y: int) -> Tuple[int, int]:
    graph[x], counter[x] = 0, 1
    q = deque([])
    q.append(x)
    while q:
        vx = q.popleft()
        for i in move:
            nx = 2 * vx if i == 2 else vx + i
            if -1 < nx < 100001 and graph[nx] == -1:
                graph[nx], counter[nx] = graph[vx] + 1, counter[vx]
                if nx != y:
                    q.append(nx)
            elif -1 < nx < 100001 and graph[nx] == graph[vx] + 1:  # 이미 방문한 지역이라도, 최단 시간값이 동일한 경우처리
                counter[nx] += counter[vx]  # +1이 아니라 이전 모든 경우의 수를 다 더해 줘야
    return graph[y], counter[y]


N, K = map(int, sys.stdin.readline().split())
move, graph, counter = [-1, 1, 2], [-1] * 100001, [-1] * 100001
for i in bfs(N, K):
    print(i)

