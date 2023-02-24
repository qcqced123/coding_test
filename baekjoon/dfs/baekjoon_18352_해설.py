from collections import deque
import sys

N, M, K, X = map(int, sys.stdin.readline().split())
graph = [[] for value in range(N + 1)] # 행렬, 테이블 구조는 무조건 이렇게 선언하자

for i in range(M):
    src, dest = map(int, sys.stdin.readline().split())
    graph[src].append(dest)

# 모든 도시에 대한 거리 초기화 => -1로 초기화해서 굳이 visited가 필요없도록 설계
# 시작 노드는 0으로 초기화
distance = [-1 for i in range(N + 1)]
distance[X] = 0

queue = deque([X])
while queue:
    v = queue.popleft() # Queue에서 빼면서 연결된 다른 노드를 삽입
    for i in graph[v]:
        if distance[i] == -1:
            distance[i] = distance[v] + 1
            queue.append(i)

check = False
for i in range(1, N + 1):
    if distance[i] == K:
        print(i)
        check = True

if not check:
    print(-1)

