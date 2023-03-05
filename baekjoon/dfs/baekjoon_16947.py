import sys
"""
[풀이 시간]
1) 00:45~01:30

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
    - 순환선에 해당 되는 노드들은 모두 0으로 일괄 처리
    - 지선의 조상이 되는 순환선 노드를 찾는다
    - 지선 조상 노드를 기준으로 지선에 속하는 노드들의 거리를 모두 구한다.
"""
N = int(sys.stdin.readline())
graph = [[0]*(N+1) for _ in range(N+1)] # 인덱스 맞춰주자

for _ in range(N+1):
    src, end = map(int, sys.stdin.readline().split())
    graph[src][end], graph[end][src] = 1, 1
