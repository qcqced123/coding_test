import sys
"""
[풀이 시간]
1) 13:00~13:30

[문제 요약]
1) 2호선 역 51개 == 노드 51개
    - 양방향 간선이 51개인 그래프
    - 순환선 부분 & 지선 부분
2) 두 노드 사이 거리 == 거쳐야 하는 간선 개수 (엣지 개수)
    - 순환선에 속하는 거리 중에서 "최소값"
3) 순환선 == 특정 역 A에서 출발해 다시 A로 돌아오는 노선을 의미

[Idea]
1) 주어진 연결 정보를 통해 테이블을 구성
    - 인덱스를 노드 번호와 일치 시키자
    - 양방향 간선이라는 것을 잊지 말자
2) 지선에 해당 되는 노드와 순환선에 해당 되는 노드 나누기
3) 지선의 시작은 리스트의 길이가 1
    - 1인 아이들을 찾아서 시작점으로 사용
    - 탐색을 하다가 len >= 3 이상이면 탐색 종료
    - 근데 어떻게 개수를 지속시키지....
    - stack overflow 뜨는 것을
    봐서 그냥 답안지 확인 하자
"""


def dfs(graph, src, result_list):
    global count
    for node in graph[src]:
        if result_list[node] == 0:
            # 다음 연결 노드가 지선인 경우
            if len(graph[node]) <= 2:
                result_list[src] += 1
                dfs(graph, node, result_list)
                result_list[src] += count
                count += 1

            # 다음 연결 노드가 순환선 시작인 경우
            if len(graph[node]) >= 3:
                result_list[src] = 1


sys.setrecursionlimit(1000000)
N = int(sys.stdin.readline())
node_list, src_list, result_list = [[]for _ in range(N+1)], [], [0] * (N+1) # src_list => 지선의 시작점 인덱스 모음
for _ in range(N):
    temp1, temp2 = map(int, sys.stdin.readline().split())
    node_list[temp1].append(temp2), node_list[temp2].append(temp1)

for i in range(1, N+1):
    if len(node_list[i]) == 1:
        src_list.append(i) # 지선 시작점 인덱스 추가

for src in src_list:
    count = 1
    dfs(node_list, src, result_list)

print(result_list[1:])
