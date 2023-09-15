import sys
"""
[요약]
1) 두 전봇대 A와 B 사이에 하나 둘씩 전깃줄을 추가하다 보니 전깃줄이 서로 교차하는 상황
    - 몇 개를 없애서 교차하지 않도록 최소한의 전깃줄 없애기
    - 시간 제한: 1초
    - 메모리: 넉넉함
    - 입력:
[전략]
1) Greedy or DP
    - 주어진 입력을 오름 차순 정렬
    - 가징 긴 증가 수열을 찾기
        - 전체 개수에서 해당 수열의 길이를 빼주기 
"""
N = int(sys.stdin.readline())
lines = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(N)])
graph = [0] * N

# 현재와 이전 것을 반복적으로 비교
for i in range(N):
    tmp_result = 0
    for j in range(i):
        if lines[i][1] > lines[j][1]:
            if tmp_result < graph[j]:
                tmp_result = graph[j]
    graph[i] = tmp_result + 1
print(N - max(graph))
